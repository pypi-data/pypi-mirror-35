class Type:
    c = ''
    format_string = ''

    def __init__(self, value=0):
        self.value = value

    def declaration(self):
        pass

    def setup(self):
        pass


class Primitive(Type):
    def declaration(self):
        return '%s %s = %d' % (self.c, self.__name__, self.value)

    def setup(self):
        return ''


class Int(Primitive):
    c = "int"
    format_string = 'i'

    def declaration(self):
        return '%s %s = %d' % (self.c, self.__name__, self.value)

    def setup(self):
        return ''


class Float(Primitive):
    c = "float"
    format_string = 'f'


class Double(Primitive):
    c = "double"
    format_string = 'd'


class Char(Primitive):
    c = "char"
    format_string = 'c'


class Void(Primitive):
    c = "void"
    format_string = 'P'


class Short(Primitive):
    c = "short"
    format_string = 'h'


class Long(Primitive):
    c = "long"
    format_string = 'q'


TYPES = [Int, Float, Double, Char, Void, Short, Long]


def parameter_types(*types):
    def editor(func):
        func.types = list(types)
        return func

    return editor


def returns(return_type):
    def editor(func):
        func.returns = return_type
        return func

    return editor
