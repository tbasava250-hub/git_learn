from random import randint 

n = randint(1,100)
play_again = "yes"
guesses = 0
print("you have only 10 attempts")
while play_again.lower() == "yes" :

    while (guesses < 10) :
    
        user = int(input("guess the number between (1 - 100) : "))
        guesses += 1
        if guesses < 10 :
            if n > user :
                print("HIGHER NUMBER PLEASE!!")    
            elif n < user :
                print("LOWER NUMBER PLEASE!!!")  
        if guesses == 10 or n == user:
            break

    if n == user :
        print(f"you have guessed the number  {n} in correctly {guesses} attempts")
    else : 
        print("better luck next time!!")
    print("\n")
    

    play_again = str(input("you want to play again(yes or no): "))
    if play_again == "yes" :
        guesses = 0
    else :
        print("thank you for playing!!!!")