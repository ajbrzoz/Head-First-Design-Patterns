class HomeTheaterFacade:
    def __init__(self, amp, tuner, dvd, cd, projector, lights, screen, popper):
        self.amp = amp
        self.tuner = tuner
        self.dvd = dvd
        self.cd = cd
        self.projector = projector
        self.lights = lights
        self.screen = screen
        self.popper = popper
    
    def watch_movie(self, movie):
        print("Get ready to watch a movie...")
        self.popper.on()
        self.popper.pop()
        self.lights.dim()
        self.screen.down()
        self.projector.on()
        self.projector.wide_screen_mode()
        self.amp.on()
        self.amp.set_dvd()
        self.amp.set_surround_sound()
        self.amp.set_volume()
        self.dvd.on()
        self.dvd.play(movie)
    
    def end_movie(self):
        print("Shutting movie theater down...")
        self.popper.off()
        self.lights.on()
        self.screen.up()
        self.projector.off()
        self.amp.off()
        self.dvd.stop()
        self.dvd.eject()
        self.dvd.off()
