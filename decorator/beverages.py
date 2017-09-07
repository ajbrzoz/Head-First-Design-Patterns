class Beverage:
    """Abstract component class"""
    
    def __init__(self, description, cost):
        self.description = description
        self.cost = cost
    
    def get_description(self):
        return self.description
    
    def get_cost(self):
        return self.cost

    
class HouseBlend(Beverage):
    def __init__(self):
        super(HouseBlend, self).__init__("House Blend Coffee", 0.89)


class DarkRoast(Beverage):
    def __init__(self):
        super(DarkRoast, self).__init__("Dark Roast Coffee", 0.99)


class Decaf(Beverage):
    def __init__(self):
        super(Decaf, self).__init__("Decaf Coffee", 1.05)


class Espresso(Beverage):
    def __init__(self):
        super(Espresso, self).__init__("Espresso Coffee", 1.99)
