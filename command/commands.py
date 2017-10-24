class Command:
    def execute(self):
        raise NotImplementedError


class GarageDoorOpenCommand(Command):
    def __init__(self, door):
        self.door = door  # Receiver
    
    def execute(self):
        self.door.up()


class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light  # Receiver
    
    def execute(self):
        self.light.on()
