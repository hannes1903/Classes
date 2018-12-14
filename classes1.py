# class Car
class Car(object):
    def __init__(self):
# self = argument, like a variable in function
# namespace—a package of variables
        self.wheels = 4
        self.doors = 5
        self.colour = 'blue'

audi = Car()
print (audi.colour)




class Car(object):
    def __init__(self, colour):
# self = argument, like a variable in function
        self.wheels = 4
        self.doors = 5
        self.colour = colour

VW = Car(colour='red')
print (VW.colour)




