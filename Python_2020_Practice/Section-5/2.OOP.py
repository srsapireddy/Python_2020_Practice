class vehicle:
    wheels = 4
    def __init__(self):
        print "vehicle"

class car(vehicle):
    def __init__(self):
        self.speed = 10
    def carVelocity(self,x):
        return x*5
    
carexample = car()
print carexample.speed
print carexample.carVelocity(3)
print carexample.wheels

