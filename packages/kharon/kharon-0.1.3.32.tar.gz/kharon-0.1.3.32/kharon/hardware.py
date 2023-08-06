# LED, Analog_Pin, Digital_pin, Switch, Pushbutton

OUT = 'OUTPUT'
IN = 'INPUT'
HIGH = 'HIGH'
LOW = 'LOW'


class Hardware:
    c = ''

    def __init__(self):
        pass

    def declaration(self, name):
        return ''

    def setup(self, name):
        return ''


class AnalogPin(Hardware):
    c = ''

    def __init__(self, pin_number, mode):
        self.pin_number = pin_number
        self.mode = mode
        super(AnalogPin, self).__init__()

    def setup(self, name):
        return 'pinMode(%d, %s)' % (self.pin_number, self.mode)


class DigitalPin(Hardware):
    c = ''


class Led(Hardware):
    c = ''


class Switch(Hardware):
    c = ''


class Button(Hardware):
    c = ''


class Servo(Hardware):
    c = ''

    def __init__(self, pin_number):
        self.pin_number = pin_number
        super(Servo, self).__init__()

    def declaration(self, name):
        return 'Servo %s;' % name

    def setup(self, name):
        return '%s.attach(%d);' % self.pin_number
