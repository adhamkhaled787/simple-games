import random;

A = int(input("Enter the upper bound of the range: "))
B = int(input("Enter the lower bound of the range: "))
secretnumber = random.randint(A,B)
print(secretnumber)
noof_guesses = int(input("Enter number of guesses"))
i = 0
notfound = True
while i < noof_guesses and notfound:
    guess = int(input("Guess the number"))
    if(guess == secretnumber):
        print(f"{secretnumber} is Correct, Congrats")
        notfound = False
    elif(guess > secretnumber):
        print(f"{guess} is too high,try again")
    else:
        print(f"{guess} is too low,try again")
    i+=1
if(notfound):
    print("You have no more guesses, game over")






