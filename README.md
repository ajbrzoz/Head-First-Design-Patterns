# Head-First-Design-Patterns
Examples from "Head First Design Patterns" implemented in Python

This repo contains code examples from the book ["Head First Design Patterns"](https://www.amazon.com/Head-First-Design-Patterns-Brain-Friendly/dp/0596007124) ported to Python. My main aim was to make them as pythonic as possible.

##### Patterns covered so far:

* Strategy
* Observer
* Decorator
* Factory
* Singleton
* Command
* Adapter

##### Remarks:

It should be noted that the book's code was written in Java and that in Python, since it allows for multiple inheritance, there's no Java-style distinction between abstract superclass and interface. 

* Strategy - There are several ways to define abstract classes in Python. Apart from the way I've used (raising an error when an unimplemented method is called from a subclass), abstract classes can be created with the [abc](https://docs.python.org/3/library/abc.html) module. There's also an interesting example in [Peter Norvig's IAQ](http://norvig.com/python-iaq.html) where he uses a separate function not only raising the appropriate error but also keeping track of the stack frame.

* Observer - This implementation is a little different from the original one: the Subject's attributes are not passed to the Observer directly as its update() function's parameters but they can be accessed through self.weather_data.

* Singleton - Here we take advantage of Python's __new__ special method.

* Adapter - Since Java doesn't support multiple inheritance, it's impossible to implement a Class Adapter. Python, on the other hand, has multiple inheritance, so I've added an implementation of this type of Adapter pattern. The class inherits from the concrete WildTurkey class as it has all the necessary methods already implemented.