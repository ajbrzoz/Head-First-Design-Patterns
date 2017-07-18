# coding=utf-8

# Encapsulated classes for Fly


# Abstract class
class FlyBehaviour:
    def fly(self):
        raise NotImplementedError()


class FlyWithWings(FlyBehaviour):
    def fly(self):
        print("I’m flying!")


class FlyNoWay(FlyBehaviour):
    def fly(self):
        print("I can't fly.")


class FlyRocketPowered(FlyBehaviour):
    def fly(self):
        print("I'm flying with a rocket!")