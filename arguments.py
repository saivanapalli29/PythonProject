# default args
def details(name,desg):
  print(f" hello my name is {name} and im {desg} engineer")
details("sai","devops")

# kw args
def details(name,desg):
  print(f" hello my name is {name} and im {desg} engineer")
details(name="sai",desg="devops")

# args
def add(*sai):
   n=0
   for i in sai:
     n=i+n
   print(n)
add(1,2,3)

# def fun():
#    print("hello")
# def fun2():
#    return "helloworld"
# fun()
# result=fun2()
# print(result)

