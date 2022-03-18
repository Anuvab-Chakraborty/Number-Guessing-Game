import random

user_input=input("enter a number:")
if user_input.isdigit():
    user_input=int(user_input)

    if user_input<=0:
        print("please enter a number greater than 0 next time")
        quit()
else:
    print("please enter a digit next time")
    quit()



random_number=random.randint(0,user_input)
#print(random_number)
guesses=0
while True:
    guesses+=1
    user_guess=input("guess a number")
    if user_guess.isdigit():
        user_guess=int(user_guess)
    else:
        print("please type a number next time")
        continue
    if user_guess==random_number:
        print("you got the correct answer")
        break
    else:
        if user_guess>random_number:
            print("you guess above the number")
        else:
            print("you guessed below the number")

print("you got it in",guesses,"number of guesses")