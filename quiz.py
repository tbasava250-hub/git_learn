print("********WELL COME TO THE QUIZ WORLD*********")
score = 0

question_bank = [
          { "text" : " 1.which language is mainly used for web page structure ","answer" : "C"},
          {"text" : " 2.what is the value of 2+3 ","answer" : "B"},
          {"text" : " 3.which one is an even number ","answer" : "A"},
          {"text" : " 4.what is the rate of my watch " , "answer" : "D"}
]
option = [
          ["A.python","B.c++","C.HTML","D.java"],
          ["A.2","B.5","C.7","D.1"],
          ["A.6","B.7","C.9","D.1"],
          ["A.500","B.600","C.700","D.900"]
]
def check_answer(guess,answer) :
    if guess == answer :
        return True
    else :
        return False

for question_num in range(len(question_bank)) :
    print(question_bank[question_num]["text"])
    for i in option[question_num]:
        print(i)

    guess = input("enter your answer(A/B/C/D): ").upper()
    is_correct = check_answer(guess,question_bank[question_num]["answer"])
     
    if is_correct :
        print("your answer is correct!!!!!")
        score += 1
    else :
        print("your entered wrong option!!!")
        
    print(f"your present score is {score}")

print(f"YOUR FINAL SCORE IS {score}")
