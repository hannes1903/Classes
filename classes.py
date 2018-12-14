
##[1,2,3,4,5]

#[1,2,3,4] == [2,3,4,5]

#len(set(a)) == 1

# set([1,1,1,1,1,2,2]) == ([0,1])


# creating blueprint / objects not only variable
# object and type (blueprint of object, object 1 = type int
# class is like type

print (type (1))
print (type (type))

print (dir(1))
# shows u methods ( = function attached to object) for object, dunder methots (double underscore), magic methods, private methods,
# never be called from the outside
#if create own, python renames it , name manngling, so you can not call it from outside
#on underscore, semi private, but please no

print ((1).__add__(2))

print((1)+(2))
# private methods only called by object itself, other can be called from outside

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

#    pass
#    pass - do nothing


class Car(object):
    def __init__(self, colour):
# self = argument, like a variable in function
        self.wheels = 4
        self.doors = 5
        self.colour = colour

VW = Car(colour='red')
print (VW.colour)


###

#class  Someclass ():
 #   def __init__(self):

# x = Someclass (a, b)
#a=1
#b=2
#print (x)

# digital ocean
