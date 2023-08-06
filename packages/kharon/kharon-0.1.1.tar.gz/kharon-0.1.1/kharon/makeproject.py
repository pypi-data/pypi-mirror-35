from pkg_resources import resource_filename, Requirement

path_to_hardware = resource_filename(Requirement.parse("kharon"), "kharon/hardware.py")
hardware = open(path_to_hardware, "r")

for line in hardware:
    print(hardware)

master = open("master.py","w+")
devices = open("devices.py","w+")
main = open("main.py","w+")
command = open("command.py","w+")