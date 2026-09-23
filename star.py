n = int(input("enter the number: "))
for i in range(1,n+1):
    print(" "*(n-i), end = "")
    print("*"*(2*i-2), end = "")
    print("\n")   


n = int(input("enter the number: "))

for i in range(1,n+1):
    if i == 1 or i == n :
        print("*"*n)
    else :
        print("*",end = "")
        print(" "*(n-2), end = "")
        print("*",end = "")
       
        print("")


n = int(input("enter the number: "))

for i in range(1,11) : 
    print(f"{n} X {11-i} = {n*(11-i)}")