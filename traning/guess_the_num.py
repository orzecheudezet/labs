import random

print("Hello. What is your name?")
name = input()

print("Well, "+name + " I am thinking of number between 1 and 20")
seceretNumber = random.randint(1, 20)

for guessesTaken in range(1, 7):
    print("Take a guess.")
    guess = int(input())

    if guess < seceretNumber:
        print("It is too low!")
    elif guess > seceretNumber:
        print("It is too high")
    else:
        print("It is your lucky day. You have guessed secretnumber :) !!!")
        break

print("You took " + str(guessesTaken) + " guesses")

if guess != seceretNumber:

    print("Game Over")