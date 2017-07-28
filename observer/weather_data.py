class Subject:
    def __init__(self):
        self.observers = []
        
    def register_observer(self, observer):
        """Attach the observer to the observers' list"""
        
        if observer not in self.observers:
            self.observers.append(observer)
    
    def remove_observer(self, observer):
        """Remove the observer from the observers' list"""
        
        try:
            self.observers.remove(observer)
        except ValueError:
            print("{} doesn't belong to the list of observers.".format(observer))
    
    def notify_observers(self):
        """Notify all observers about a change in the subject's state"""
        
        for observer in self.observers:
            observer.update()

    
class WeatherData(Subject):
    def __init__(self):
        super(WeatherData, self).__init__()
        self.temperature = 0
        self.humidity = 0.0
        self.pressure = 0.0
    
    def measurements_changed(self):
        self.notify_observers()
        
    def set_measurements(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.measurements_changed()
