
class Human:
    def __init__(self, name,age):
        self.name = name
        self.age = age
    def eat(self):
        print("i can eat")
    def drink(self):
        print("i can drink")
    def display(self):
        print(f"my name is {self.name} and my age is {self.age}")
class Male(Human):
    def __init__(self, name,age,location):
        Human.__init__(self,name,age)
        self.location = location
    def gym(self):
        print("i do gym daily")
    def crcket(self):
        print("i play crcket daily")
class Female(Human):
    def __init__(self, name,age,can_dance):
        super().__init__(name,age)  # we can use super().methodnm or Class.methodname
        self.can_dance = can_dance
    def sleep(self):
        print("i sleep 12 hours daily")
    def makeup(self):
        print("i will not go outside without makeup")
    def display(self):
        #Human.display(self)    # or
        super().display()
        print(f"can i dance{self.can_dance}")


male = Male("sai",25,"Bhimavaram")
female=Female("Ratnam",10,True)

female.display()

# print(female.name)
# print(female.can_dance)

# print(male.name)
# female = Female()

