def add(*args):
    number = 0
    for i in args:
        number = number + i
    print(number)
add(2,5,3,9,5)

def calculate(**kwargs):
    print(kwargs)
calculate(add=3, multiply = 5)

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")

my_car = Car(make = "Nissan")
print(my_car.model)
