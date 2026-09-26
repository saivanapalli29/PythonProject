def main():
    def add(a,b):
        return a+b
    def subtract(a,b):
        return a-b
    def multiply(a,b):
        return a*b
    def divide(a,b):
        return a/b
    operation_dict = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide
    }
    num1=float(input("enter first number: "))
    for i in operation_dict:
        print(i)
    continue_flag=True
    while continue_flag:
        user_operation = input("choose your operator: ")
        num2=float(input("enter second number: "))
        calculator=operation_dict[user_operation]
        calc=calculator(num1,num2)
        print(calc)
        repeat=input("Do you want to calculate another number type y or continue with new calculation type n and for exit type x: ").lower()
        if repeat=="y":
            num1=calc
        elif repeat=="n":
            #continue_flag=False
            main()
        else:
           continue_flag=False
           print("bye")
main()
