# write a program that plays rock, paper, scissors against the computer
# 1. When the program begins, it should generate a random number in the range of 1 to 3
#       where 1=rock, 2=paper, 3=scissors
# 2. The user enters a choice of "rock", "paper" or "scissors" at the keyboard
# 3. The computer's choice is displayed
# 4. The winner is determined and the result is displayed: rock > scissors > paper > rock
# If both players choose the same value, play again
import random                  # import the library

# define GLOBAL CONSTANTS
# python 'style guidelines' recommend global constants should all be all UPPER CASE with underscore
ROCK = 1
PAPER = 2
SCISSORS = 3


# the main() function has the main game logic
def main():
    # display welcome message
    print ('welcome! Lets play Rock, Paper, Scissors')

    computer_choice = get_computer_choice()              # gets a random choice for the computer
    player_choice = get_player_choice ()                 # get the player's choice
    display_results(computer_choice, player_choice)      # display an appropriate response

    while computer_choice == player_choice:
        computer_choice = get_computer_choice()              # gets a random choice for the computer
        player_choice = get_player_choice ()                 # get the player's choice
        display_results(computer_choice, player_choice)      # display an appropriate response

    # display an exit message
        print('\nThanks for playing.')


# the ger_computer_choice() function return a random value between 1 and 3
def get_computer_choice():
    return random.randint(1, 3)                # gets a number between 1 and 3 and returns it


# get the players_choice() and validate it -- make sure it is 1, 2, 3
def get_player_choice():
    choice = '0'          # not be a valid answer , so the loop will run at least once

    # this is my validation loop to ask for and validate the answer:
    while  choice != '1' and choice != '2' and choice != '3':           # test for bad data
        print('\nWhat will you choose:')
        print('   1. rock')
        print('   2. paper')
        print('   3. scissors')
        choice = input('? ').strip()         # strip() off any extra whitespace

    # once we exit the loop the choice has been validated
    return int(choice)                # converting to an interger and returning it


# display the results of what was chossen and who wins
def display_results(computer, player):
    print('\nThe computer choose', translate(computer), 'and your choose', translate(player))
    if player == computer:
        print('no winner try again.')
    elif computer == ROCK:
        if player == PAPER:
            print('Paper covers rock. You win!')
        else:          # only other option is player == SCISSORS
            print('Rock breaks scissors. Computer wins.')
    elif computer == PAPER:
        if player == ROCK:
            print('Paper covers rock. Computer wins.')
        else:         # player == SCISSORS
            print('Scissors cuts paper. You win!')
    else:     # computer is scissors
        if player == PAPER:
            print('Scissors cuts paper. Computer wins.')
        else:       # player has rock
            print('Rock breaks scissors. You win!')


# translate() takes the numeric value and return the corresponding string
def translate(numeric_choice):
    if numeric_choice == ROCK:
        return 'rock'
    elif numeric_choice == PAPER:
        return 'paper'
    elif numeric_choice == SCISSORS:
        return 'Scissors'
    else:
        return'invalid value'               # if everything is working properly, I will never see this


main()
