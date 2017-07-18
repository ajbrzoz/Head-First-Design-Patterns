# coding=utf-8

# Encapsulated classes for Quack behaviour


# Abstract class
class QuackBehaviour:
    def quack(self):
        raise NotImplementedError()


class Quack(QuackBehaviour):
    def quack(self):
        print("Quack, quack!")


class MuteQuack(QuackBehaviour):
    def quack(self):
        print("<< Silence >>")


class Squeak(QuackBehaviour):
    def quack(self):
        print("Squeak!")
