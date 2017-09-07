from beverages import Beverage

class CondimentDecorator(Beverage):
    """Abstract decorator class"""
    
    def __init__(self, description, cost, beverage):
        super(CondimentDecorator, self).__init__(description, cost)
        self.beverage = beverage
    
    def get_description(self):
        return self.beverage.get_description() + ", " + self.description
    
    def get_cost(self):
        return self.beverage.get_cost() + self.cost


class SteamedMilk(CondimentDecorator):
    def __init__(self, beverage):
        super(SteamedMilk, self).__init__("Steamed Milk", 0.10, beverage)


class Mocha(CondimentDecorator):
    def __init__(self, beverage):
        super(Mocha, self).__init__("Mocha", 0.20, beverage)


class Soy(CondimentDecorator):
    def __init__(self, beverage):
        super(Soy, self).__init__("Soy", 0.15, beverage)


class Whip(CondimentDecorator):
    def __init__(self, beverage):
        super(Whip, self).__init__("Whip", 0.10, beverage)
