class Vehicle:
    def __init__(self,mfd):
        print("I am a Vehicle")
        self.num_tyres = 4
        self.tyre_name = "mrf"
        self.mfd = mfd

    def start(self):
        print("I can start")


class Car:

    def __init__(self, car_name, model):
        print("I am a Car")
        self.car_name = car_name
        self.model = model

    def gear(self):
        print("I have 5gears")


class Toyota(Vehicle, Car):
    def __init__(self, name, age,mf_date, carnm, modl):
        print("I am a Toyota")
        Car.__init__(self, carnm, modl)  #classnm.methnn(self,arg1,...)
        Vehicle.__init__(self,mf_date)
        self.name = name
        self.age = age

    def gear(self):
        print("I can gear")


car_1 = Toyota("sai",25,2026, "bs6", "toyota")  #based on parameters we have to pass the args
car_1.start()
Car.gear(car_1)  #classnm.methnm(objnm)
car_1.gear()
print(car_1.name)
print(car_1.car_name)
print(car_1.num_tyres)
print(car_1.mfd)
