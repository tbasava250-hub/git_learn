print("=====VOWELS WORLD======")
vowels = ('a','e','i','o','u')

while True :
    alphabet = input("enter the alphabet (0 for quit)!!!")

    if alphabet == '0' :

        print("thank you for using our service!!!!")
        break

    elif alphabet.isalpha() and len(alphabet) == 1:

        if alphabet.lower() in vowels :
            print(f"entered alphabet {alphabet} is vowel...")

        else :
            print(f"entered alphabet {alphabet} is consonant...")
         




