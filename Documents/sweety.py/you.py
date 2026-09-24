import math 
def prime_checker(number) :
    is_prime = True
    if number == 1:
        is_prime = False
    for i in range(2,math.floor(number/2)) :
        if number %i == 0 :
            is_prime = False
    if is_prime :
        print("GIVEN NUMBER IS PRIME NUMBER!!")
    else :
        print("GIVEN NUMBER IS NOT A PRIIME NUMBER!!")

n = int(input("enter a number want to check prime or not: "))
prime_checker(n)