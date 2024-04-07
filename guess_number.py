import random
num = random.randint(1,10)
guess = int(input("Guess a number beyween 1 to 10: \n"))
tries = 1

while guess != num:
    if guess < num:
        print("Your Guess is too Low!!")
    elif guess > num:
        print("Your Guess is too High!!")

    guess = (int(input("Guess Again!! \n")))
    tries += 1

print("Congrats!! the number {} guessed is right in {} tries".format(guess,tries))