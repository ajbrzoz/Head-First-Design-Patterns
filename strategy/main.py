# coding=utf-8

# STRATEGY pattern


from .ducks import MallardDuck, ModelDuck
from .fly_behaviours import FlyRocketPowered


if __name__ == "__main__":
    mallard = MallardDuck()
    mallard.perform_quack()
    mallard.perform_fly()

    model = ModelDuck()
    model.perform_fly()
    model.set_fly_behaviour(FlyRocketPowered())
    model.perform_fly()
