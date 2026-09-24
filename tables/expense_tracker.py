expenses = []
the = True
while the:
    print("\n====expenses tracker=====")
    print("1.Add item")
    print("2.view item")
    print("3.show total")
    print("4.exit")

    choice = input("enter your choice")

    if choice == "1":
        item = input("enter the item to be add: ")
        amount = float(input("enter the cost: "))

        expenses.append((item,amount))
        print("item added succesfully!")
    elif choice == "2":
        print("\nYour expenses")
        for item,amount in expenses:
            print(item,"$",amount)

    elif choice == "3":
        total = 0
        for item,amount in expenses:
            total += amount
        print("total expense is ",total)
    elif choice == "4":
        print("Thank you!!!!")
        the = False
    else :
        print("invalid choice!!")