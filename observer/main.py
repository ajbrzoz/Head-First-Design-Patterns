from weather_data import WeatherData
from observers import CurrentConditionsDisplay

if __name__ == "__main__":
    w_data = WeatherData()
    current_display = CurrentConditionsDisplay(w_data)
    
    w_data.set_measurements(80, 65, 30.4)
    w_data.set_measurements(82, 70, 29.2)
    w_data.set_measurements(78, 90, 29.2)
