import math



def prime_check(n):
    is_prime=True
    if n < 2:
        is_prime=False

    for i in range(2,math.ceil(n/2)+1):
        if n%i==0:
            is_prime=False
    if is_prime:
        return "number is prime"
    else:
        return "number is not prime"

number=int(input("enter a number:"))

result=prime_check(n=number)
print(result)