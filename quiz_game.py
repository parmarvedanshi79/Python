questions=(("Which planet in our solar system is known as the 'Red Planet'?"),
           ("What is the name of the galaxy that contains Earth?"),
           ("Who is credited with painting the Mona Lisa?:"),
           ("Which animal is known for having the longest neck and spots?"))
options=(("A. Venus","B. Mars","C. Jupiter","D. Saturn"),
         ("A. Andromeda","B. Sombrero","C. The Milky Way","D. Triangulum"),
         ("A. Vincent van Gogh","B. Pablo Picasso","C. Claude Monet","D. Leonardo da Vinci"),
         ("A. Zebra","B. Camel","C. Giraffe","D. Ostrich"))
guesses=[]
answers=("B","C","D","C")
score=0
question_num=0

for question in questions:
    print("------------------")
    print(question)
    for option in options[question_num]:
         print(option)
    guess=input("Enter (A,B,C,D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
         score+=1
         print("Correct!")
    else:
         print("Incorrect!")
         print(f"The correct answer is {answers[question_num]}")
    question_num+=1
print()
print("Result")
print("Guesses: ", end="")
for guess in guesses:
    print(guess, end="")
print()
print("Answers: ", end="")
for answer in answers:
     print(answer, end="")
print()

score=int(score/len(questions)*100)
print(f"Your score is {score}")
   

