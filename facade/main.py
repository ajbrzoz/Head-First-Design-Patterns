from .components import *
from .facade import HomeTheaterFacade
    

if __name__ == "__main__":
    
    amp = Amplifier()
    tuner = Tuner()
    dvd = DvdPlayer()
    cd = CdPlayer()
    projector = Projector()
    lights = TheaterLights()
    screen = Screen()
    popper = PopcornPopper()
    
    home_theater = HomeTheaterFacade(amp, tuner, dvd, cd, projector, lights, screen, popper)
    home_theater.watch_movie("Raiders of the Last Ark")
    home_theater.end_movie()
