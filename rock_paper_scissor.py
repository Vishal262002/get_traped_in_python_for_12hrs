import random 

def play_game():
    options = ['rock','paper','scissor']
    computer_choice = random.choice(options)
    user_choice = input("Enter ('rock','paper','scissor') to start the game: \n").lower()

    print("You Chose: {}".format(user_choice))
    print("Computer_Chose: {}".format(computer_choice))

    if user_choice not in options:
        print("Invalid Choice, please select either rock, paper, scissor \n")
        return

    if (user_choice == 'rock' and computer_choice == 'paper') or \
        (user_choice == 'paper' and computer_choice == 'scissor') or \
            (user_choice == 'scissor' and computer_choice == 'rock'):
        print("Hurry!! You Win")
    else:
        print("Oops!! computer wins")

play_game()