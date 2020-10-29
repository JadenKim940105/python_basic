# 파이썬은 다중상속 허용함

class Car:
    """Parent Class"""
    def __init__(self, tp, color):
        self.type = tp
        self.color = color

    def show(self):
        return 'Car Class "Show Method"'

class BMWCar(Car):
    """Sub Class"""
    def __init__(self, car_name, tp, color):
        super().__init__(tp, color)
        self.car_name = car_name

    def show_model(self):
        return "Your Car Name: %s" % self.car_name


class BenzCar(Car):
    """Sub Class"""
    def __init__(self, car_name, tp, color):
        super().__init__(tp, color)
        self.car_name = car_name

    def show_model(self):
        return "Your Car Name: %s" %self.car_name

    def show(self):
        print(super().show())
        return "Your Car Name: %s" % self.car_name



model1 = BMWCar("520d", "sedan", "red")

print(model1.color)
print(model1.type)
print(model1.car_name)
print(model1.show())
print(model1.show_model())

model2 = BenzCar("e-class", "sedan", "red")
print(model2.show())
print(model2.show_model())

model3 = BenzCar("s-class", "sedan", "silver")
print(model3.show())

