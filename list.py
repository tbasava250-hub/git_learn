n = [2,3,4,5,6,7,8,9,2,5,10]
target = int(input("enter the numeber: "))
for i in range(len(n)):
  for j in range(len(n)):
    if i+j == target:
      print(f"{target},({i},{j})")

num = [4,0,3,5,0,6,7,0,7,0,0,3]
for i in num:
  num.remove(0)
  num.append(0)

print(num)