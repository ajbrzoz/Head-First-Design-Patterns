import unittest
import io
import sys

from strategy.ducks import MallardDuck, ModelDuck
from strategy.fly_behaviours import FlyRocketPowered

from observer.weather_data import WeatherData
from observer.observers import CurrentConditionsDisplay

from decorator.beverages import Espresso, DarkRoast
from decorator.condiments import Mocha, Whip

from factory.stores import NYPizzaStore, ChicagoPizzaStore

from singleton.boiler import ChocolateBoiler

from command.commands import LightOnCommand
from command.receivers import Light
from command.remote import SimpleRemoteControl


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


class DecoratorTestCase(unittest.TestCase):
    
    def test_component_without_decorators(self):
        beverage = Espresso()
        self.assertEqual(beverage.get_cost(), 1.99)
        
    def test_component_with_decorators(self):
        beverage2 = DarkRoast()
        beverage2 = Mocha(beverage2)
        beverage2 = Mocha(beverage2)
        beverage2 = Whip(beverage2)
        self.assertEqual(beverage2.get_cost(), 1.49)


class FactoryTestCase(unittest.TestCase):
    
    def setUp(self):
        self.ny_store = NYPizzaStore()
        self.chicago_store = ChicagoPizzaStore()
        
    def test_factory(self):
        pizza1 = self.ny_store.order_pizza("cheese")
        pizza2 = self.chicago_store.order_pizza("cheese")
        self.assertEqual(pizza1.name, "NY Style Sauce and Cheese Pizza")
        self.assertEqual(pizza2.name, "Chicago Style Deep Dish Cheese Pizza")


class SingletonTestCase(unittest.TestCase):
    def setUp(self):
        self.cb1 = ChocolateBoiler()
        self.cb2 = ChocolateBoiler()
    
    def test_singleton(self):
        self.assertEqual(self.cb1, self.cb2)


class CommandTestCase(unittest.TestCase):
    def setUp(self):
        self.captured = io.StringIO()
        
        self.remote = SimpleRemoteControl()
        self.light = Light()
        self.light_on = LightOnCommand(self.light)
    
    def test_simple_remote(self):
        self.remote.set_command(self.light_on)
        sys.stdout = self.captured
        self.remote.button_was_pressed()
        sys.stdout = sys.__stdout__
        self.assertEqual(self.captured.getvalue().strip(), "Light is On")

if __name__ == '__main__':
    unittest.main()
