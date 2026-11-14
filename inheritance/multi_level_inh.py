
class Human:
    def __init__(self, name):
        self.name = name
        self.age=25
    def eat(self):
        print("eat from Human")
    def work(self):
        print("work from Human")
class Male(Human):
    def __init__(self, num_heart):
        self.heart=num_heart

    def walk(self):
        print("walk from Male")
class Boy(Male):
    def __init__(self, name,num_heart,num_eyes):
        Human.__init__(self, name)
        Male.__init__(self, num_heart)
        self.eyes=num_eyes

    def play(self):
        print("play from Boy")
    def work(self):
        Human.work(self) #  or super().work() super() --> parent class  self --> Means person1(obj)
        #super().work()
        print("work from Boy")
    def display(self):
        print(f"My name is {self.name} and I am {self.age} years old and i have {self.eyes} eyes and ")



person1 = Boy("sai",1,2)
#Human.work(person1)  # to access the parent class methods or attributes
print(person1.name)
print(person1.heart)
print(person1.eyes)