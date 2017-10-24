class Command:
    def execute(self):
        raise NotImplementedError


class GarageDoorUpCommand(Command):
    def __init__(self, door):
        self.door = door  # Receiver
    
    def execute(self):
        self.door.up()


class GarageDoorDownCommand(Command):
    def __init__(self, door):
        self.door = door  # Receiver
    
    def execute(self):
        self.door.down()


class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light  # Receiver
    
    def execute(self):
        self.light.on()


class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light  # Receiver
    
    def execute(self):
        self.light.off()


class CeilingFanOnCommand(Command):
    def __init__(self, cf):
        self.cf = cf
    
    def execute(self):
        self.cf.on()


class CeilingFanOffCommand(Command):
    def __init__(self, cf):
        self.cf = cf
    
    def execute(self):
        self.cf.off()


class StereoOnCommand(Command):
    def __init__(self, stereo):
        self.stereo = stereo
    
    def execute(self):
        self.stereo.on()


class StereoOffCommand(Command):
    def __init__(self, stereo):
        self.stereo = stereo
    
    def execute(self):
        self.stereo.off()


class StereoSetCdCommand(Command):
    def __init__(self, stereo):
        self.stereo = stereo
    
    def execute(self):
        self.stereo.set_cd()
        

class NoCommand:
    pass