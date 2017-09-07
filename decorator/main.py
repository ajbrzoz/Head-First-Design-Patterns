from beverages import Espresso, DarkRoast, HouseBlend
from condiments import Mocha, Soy, Whip

if __name__ == "__main__":
    
    # simple espresso (no decorators)
    beverage = Espresso()
    print(beverage.get_description() + " $" + str(beverage.get_cost()))
    
    # double mocha dark roast with whip
    beverage2 = DarkRoast()
    beverage2 = Mocha(beverage2)
    beverage2 = Mocha(beverage2)
    beverage2 = Whip(beverage2)
    print(beverage2.get_description() + " $" + str(beverage2.get_cost()))
    
    # soy mocha house blend with whip
    beverage3 = HouseBlend()
    beverage3 = Soy(beverage3)
    beverage3 = Mocha(beverage3)
    beverage3 = Whip(beverage3)
    print(beverage3.get_description() + " $" + str(beverage3.get_cost()))
