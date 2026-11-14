
class A:
    def display(self):
        print("I am a A class")
class B(A):     # A and B are single inh
    def display(self):
        print("I am a B class")
class C:
    def display(self):
        print("I am a C class")
class D(B,C):  # B,C and D are multiple inh
    def display(self):
        A.display(self)
        super().display()
        super(A, self).display()  # its looking after B (if you mention C looking after C) in mro order
        print("I am a D class")

sai=D()
sai.display()
print(D.mro())  #classnm .mro()