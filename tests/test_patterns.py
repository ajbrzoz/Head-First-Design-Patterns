import unittest
import io
import sys

from strategy.ducks import MallardDuck, ModelDuck
from strategy.fly_behaviours import FlyRocketPowered

from observer.weather_data import WeatherData
from observer.observers import CurrentConditionsDisplay

class StrategyTestCase(unittest.TestCase):
    
    def setUp(self):
        self.captured = io.StringIO()

        self.mallard = MallardDuck()
        self.model = ModelDuck()
    
    def test_mallard_quack(self):
        sys.stdout = self.captured
        self.mallard.perform_quack()
        sys.stdout = sys.__stdout__
        self.assertEqual(self.captured.getvalue().strip(), "Quack, quack!")

    def test_mallard_fly(self):
        sys.stdout = self.captured
        self.mallard.perform_fly()
        sys.stdout = sys.__stdout__
        self.assertEqual(self.captured.getvalue().strip(), "I’m flying!")
        
    def test_model_fly(self):
        sys.stdout = self.captured
        self.model.perform_fly()
        sys.stdout = sys.__stdout__
        self.assertEqual(self.captured.getvalue().strip(), "I can't fly.")
        
    def test_model_fly_after_setting(self):
        self.model.set_fly_behaviour(FlyRocketPowered())
        sys.stdout = self.captured
        self.model.perform_fly()
        sys.stdout = sys.__stdout__
        self.assertEqual(self.captured.getvalue().strip(), "I'm flying with a rocket!")


class ObserverTestCase(unittest.TestCase):

    def setUp(self):
        self.w_data = WeatherData()
        self.current_display = CurrentConditionsDisplay(self.w_data)
        
    def test_changing_measurements(self):
        """Test if the subject's and observers' values are equal"""
        temperature_values = [80, 82, 78]
        humidity_values = [65, 70, 90]
        pressure_values = [30.4, 29.2, 29.2]
        
        for t, h, p in zip(temperature_values, humidity_values, pressure_values):
            self.w_data.set_measurements(t, h, p)
            self.assertEqual(self.current_display.temperature, t)
            self.assertEqual(self.current_display.humidity, h)
