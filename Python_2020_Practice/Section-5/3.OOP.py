class vehicle:
    wheels = 4
    def carVelocity(self,x):
        return x*5
    def __init__(self):
        print "vehicle"

class car(vehicle):
    def __init__(self):
        self.speed = 10
    
carexample = car()
print carexample.speed
print carexample.carVelocity(3)
print carexample.wheels

#The self variable refers to the object itself.
# __init__ is what is called as a constructor in other OOP languages such as C++/Java. The basic idea is that it is a special method which is automatically called when an object of that Class is created
