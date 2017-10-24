class Command:
    def execute(self):
        raise NotImplementedError
    
    def undo(self):
        raise NotImplementedError


class GarageDoorUpCommand(Command):
    def __init__(self, door):
        self.door = door  # Receiver
    
    def execute(self):
        self.door.up()
        
    def undo(self):
        self.door.down()


class GarageDoorDownCommand(Command):
    def __init__(self, door):
        self.door = door  # Receiver
    
    def undo(self):
        self.door.up()


class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light  # Receiver
    
    def execute(self):
        self.light.on()
        
    def undo(self):
        self.light.off()


class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light  # Receiver
    
    def execute(self):
        self.light.off()
        
    def undo(self):
        self.light.on()


class CeilingFanOnCommand(Command):
    def __init__(self, cf):
        self.cf = cf
    
    def execute(self):
        self.cf.on()
        
    def undo(self):
        self.cf.off()


class CeilingFanOffCommand(Command):
    def __init__(self, cf):
        self.cf = cf
    
    def execute(self):
        self.cf.off()
        
    def undo(self):
        self.cf.on()


class CeilingFanHighCommand(Command):
    def __init__(self, cf):
        self.cf = cf
        self.prev_speed = 0
    
    def execute(self):
        self.prev_speed = self.cf.speed
        self.cf.off()
    
    def undo(self):
        if self.prev_speed == self.cf.HIGH:
            self.cf.high()
        elif self.prev_speed == self.cf.MEDIUM:
            self.cf.medium()
        elif self.prev_speed == self.cf.LOW:
            self.cf.low()
        elif self.prev_speed == self.cf.OFF:
            self.cf.off()


class StereoOnCommand(Command):
    def __init__(self, stereo):
        self.stereo = stereo
    
    def execute(self):
        self.stereo.on()
        
    def undo(self):
        self.stereo.off()


class StereoOffCommand(Command):
    def __init__(self, stereo):
        self.stereo = stereo
    
    def execute(self):
        self.stereo.off()
        
    def undo(self):
        self.stereo.on()


class StereoSetCdCommand(Command):
    def __init__(self, stereo):
        self.stereo = stereo
    
    def execute(self):
        self.stereo.set_cd()
        
    def undo(self):
        pass
        

class NoCommand(Command):
    def execute(self):
        pass
    
    def undo(self):
        pass