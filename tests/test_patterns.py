import unittest
import io
import sys

from strategy.ducks import MallardDuck, ModelDuck
from strategy.fly_behaviours import FlyRocketPowered

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
