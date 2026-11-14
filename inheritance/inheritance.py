class Human:
     def __init__(self,age):
         self.num_eyes=2
         self.num_teeth=32
         self.age=age
     def work(self):
         print("i can do work")
     def coding(self):
        print("i can do code")
class sai(Human):
    def __init__(self,name,age):
        super().__init__(age)
        self.num_nose=1
        self.name=name
    def eat(self):
        print("i can eat")
    def coding(self):
        super().coding()
        print("i can write python")
person_1=sai("sai",25)
person_1.work()
person_1.coding()
print(person_1.num_eyes)
print(person_1.num_teeth)
print(person_1.name)
print(person_1.age)
