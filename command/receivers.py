class Light:
    def __init__(self, location=""):
        self.location = location
    
    def on(self):
        print("Light is On")
    
    def off(self):
        print("Light is Off")


class GarageDoor:
    def __init__(self, location=""):
        self.location = location
    
    def up(self):
        print("Garage Door is Open")
    
    def down(self):
        print("Garage Door is Closed")
    

class Stereo:
    def __init__(self, location=""):
        self.location = location
    
    def on(self):
        print("Stereo is On")
    
    def off(self):
        print("Stereo is Off")

    def set_cd(self):
        print("Stereo is set for CD input")

    def set_volume(self, vol):
        print("Stereo volume set to ", vol)


class CeilingFan:
    HIGH = 3
    MEDIUM = 2
    LOW = 1
    OFF = 0
    
    def __init__(self, location="", speed=OFF):
        self.location = location
        self.speed = speed
        
    def high(self):
        self.speed = self.HIGH

    def medium(self):
        self.speed = self.MEDIUM
        
    def low(self):
        self.speed = self.LOW
    
    def on(self):
        print("Ceiling Fan is On")
    
    def off(self):
        print("Ceiling Fan is Off")
        self.speed = self.OFF
