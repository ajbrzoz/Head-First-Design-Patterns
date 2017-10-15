from .pizzas import *

class PizzaStore:
    def order_pizza(self, kind):
        pizza = self.create_pizza(kind)
        
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        
        return pizza
    
    @staticmethod
    def create_pizza(kind):
        raise NotImplementedError()


class NYPizzaStore(PizzaStore):
    @staticmethod
    def create_pizza(kind):
        
        pizza = None
        
        if kind == "cheese":
            pizza = NYStyleCheesePizza()
        elif kind == "pepperoni":
            pizza = NYStylePepperoniPizza()
        elif kind == "clam":
            pizza = NYStyleClamPizza()
        elif kind == "veggie":
            pizza = NYStyleVeggiePizza()
        
        return pizza


class ChicagoPizzaStore(PizzaStore):
    @staticmethod
    def create_pizza(kind):
        
        pizza = None
        
        if kind == "cheese":
            pizza = ChicagoStyleCheesePizza()
        elif kind == "pepperoni":
            pizza = ChicagoStylePepperoniPizza()
        elif kind == "clam":
            pizza = ChicagoStyleClamPizza()
        elif kind == "veggie":
            pizza = ChicagoStyleVeggiePizza()
        
        return pizza