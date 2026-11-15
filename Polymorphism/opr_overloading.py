class Addition1:
    def __init__(self, a,b):
        self.a = a
        self.b = b
    def __add__(self, other):
            return (f"{self.a + other.a} {self.b + other.b}")


add1=Addition1(10,20)
add2=Addition1(30,40)

print (add1 + add2)
