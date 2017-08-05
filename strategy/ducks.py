# Abstract Duck class with subclasses


from fly_behaviours import FlyNoWay, FlyWithWings
from quack_behaviours import Quack


# Abstract Duck class
class Duck:
    def __init__(self):
        self.quack_behaviour = None
        self.fly_behaviour = None
    
    def perform_quack(self):
        self.quack_behaviour.quack()
    
    def perform_fly(self):
        self.fly_behaviour.fly()
    
    def set_quack_behaviour(self, qb):
        self.quack_behaviour = qb
    
    def set_fly_behaviour(self, fb):
        self.fly_behaviour = fb
    
    def swim(self):
        print("All ducks float, even decoys!")
    
    def display(self):
        raise NotImplementedError()


class ModelDuck(Duck):
    def __init__(self):
        super(Duck, self).__init__()
        self.fly_behaviour = FlyNoWay()
        self.quack_behaviour = Quack()
    
    def display(self):
        print("I'm a model duck")


class MallardDuck(Duck):
    def __init__(self):
        super(MallardDuck, self).__init__()
        self.quack_behaviour = Quack()
        self.fly_behaviour = FlyWithWings()
