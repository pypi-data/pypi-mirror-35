import inspect
import re
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
    (r' and ', r'&&'),
    (r' or ', r'||'),
    (r' not ', r'!'),
]


def ferry_function(func, device):
    name = '%s_%s' % (device.__name__, func.__name__)
    parameters = ''
    for parameter, p_type in zip([p for p in list(inspect.signature(func).parameters)[1:]], func.types):
        parameters += '%s %s, ' % (p_type.c, parameter)
    parameters = parameters[:-2]

    header = '%s %s(%s){\n' % (func.returns.c, name, parameters)
    lines = inspect.getsourcelines(func)[0]

    body = ''
    for line, next_line in zip(lines[3:], lines[4:] + ['']):
        print(line)
        ind = count_indent(line)
        next_ind = count_indent(next_line)

        for replacement in REPLACEMENTS:
            print(replacement)
            line = re.sub(replacement[0], replacement[1], line)

        print(line)
        body += line
        if next_ind > ind:
            body += '{' * int((next_ind - ind) / 4)
        if next_ind < ind:
            body += '}' * int((ind - next_ind) / 4)

    return header + body
