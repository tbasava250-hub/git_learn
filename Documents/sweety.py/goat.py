import random
letters = {'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
numbers = { '1','2','3','4','5','6','7','8','9','0'}
symbols = { '!','@','#','$','%','&','*','(',')'}
n_letter = int(input("enter how much letter want in password: "))
n_number = int(input("enter how much numbers want in password: "))
n_symbols = int(input("enter how much symbols want in password: "))
password = " "
for i in range(1,n_letter+1) :
    A = random.choice(list(letters))
    password += A
for i in range(1,n_number+1) :
    A = random.choice(list(numbers))
    password += A
for i in range(1,n_symbols+1) :
    A = random.choice(list(symbols))
    password += A 

print(password)   