import inspect
import re
from pkg_resources import resource_filename, Requirement
from .c_types import TYPES


def count_indent(line):
    counter = re.compile(r'(^\s+)')
    match = counter.match(line)
    return 0 if match is None else len(match.expand(r'\1'))


REPLACEMENTS = [
    (r'\s+', r' '),
    *[(r's*([a-zA-Z_][a-zA-Z_0-9]*)\s*=\s*%s\(\)' % type_class.__name__,
       r'%s \1;' % type_class.c) for type_class in TYPES],
    (r'(s*[a-zA-Z_][a-zA-Z_0-9]*\s*=\s*.*?)$', r'\1;'),
    (r'(s*return\s*.*?)$', r'\1;'),
    (r'([a-z]+)\s(.*?):', r'\1(\2)'),
    (r's*print\((.*?)\)', r'Serial.println(\1);'),
    (r' and ', r'&&'),
    (r' or ', r'||'),
    (r' not ', r'!'),
]


def make_function_head(func, device):
    name = '%s_%s' % (device.__name__, func.__name__)
    parameters = ''
    for parameter, p_type in zip([p for p in list(inspect.signature(func).parameters)[1:]], func.types):
        parameters += '%s %s, ' % (p_type.c, parameter)
    parameters = parameters[:-2]

    header = '%s %s(%s)\n' % (func.returns.c, name, parameters)

    return header


def ferry_function(func, device):
    header = make_function_head(func, device)
    lines = inspect.getsourcelines(func)[0]

    body = '{'
    for line, next_line in zip(lines[3:], lines[4:] + ['']):
        ind = count_indent(line)
        next_ind = count_indent(next_line)

        for replacement in REPLACEMENTS:
            line = re.sub(replacement[0], replacement[1], line)

        body += line
        if next_ind > ind:
            body += '{' * int((next_ind - ind) / 4)
        if next_ind < ind:
            body += '}' * int((ind - next_ind) / 4)

        body += '\n\n'
    return header + body


def get_functions(device):
    functions = inspect.getmembers(device, lambda a: (inspect.isroutine(a)))
    functions = [a for a in functions if not (a[0].startswith('__') and a[0].endswith('__'))]
    return functions


def get_members(device):
    members = inspect.getmembers(device, lambda a: not (inspect.isroutine(a)))
    members = [a for a in members if not (a[0].startswith('__') and a[0].endswith('__'))]
    return members


def assemble(module):
    devices = inspect.getmembers(module, inspect.isclass)
    template = open(resource_filename(Requirement.parse("kharon"), "kharon/template.ino")).read()
    dev_ino = template + '\n'

    for device in devices:
        members = get_members(device)
        functions = get_functions(device)
        print(members)
        print(functions)

        declarations = ''
        setup = ''
        for member in members:
            declarations += member.declaration() + ';\n'
            setup += member.setup() + ';\n'
        dev_ino = re.sub('//GLOBALS', declarations, dev_ino)
        dev_ino = re.sub('//SETUP', setup, dev_ino)

        statement = ''
        implementation = ''
        for func in functions:
            statement += make_function_head(func, device) + ';\n'
            implementation += ferry_function(func, device) + '\n'
        dev_ino = re.sub('//FUNCTIONS', statement + '\n' + implementation, dev_ino)

        print(dev_ino)
