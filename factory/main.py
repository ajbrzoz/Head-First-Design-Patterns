from .stores import NYPizzaStore, ChicagoPizzaStore

if __name__ == "__main__":

    ny_store = NYPizzaStore()
    chicago_store = ChicagoPizzaStore()
    
    pizza = ny_store.order_pizza("cheese")
    print("Ethan ordered a {}.\n".format(pizza.name))

    pizza = chicago_store.order_pizza("cheese")
    print("Joel ordered a {}.\n".format(pizza.name))
