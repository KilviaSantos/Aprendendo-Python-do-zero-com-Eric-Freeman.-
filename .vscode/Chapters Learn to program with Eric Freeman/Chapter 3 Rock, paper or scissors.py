# Import the random module.
import random

# Configure the winner variable.
winner = ''

# The computer randomly chooses rock, paper, or scissors through the
# random.choice.
choices = ['rock', 'paper', 'scissors']
computer_choice = random.choice(choices)

# Identifies if the user made an invalid choice and the while prompts again
# until it's a valid input. 
user_choice = ''
while (user_choice != 'rock' and 
        user_choice != 'paper' and
        user_choice != 'scissors') :
    user_choice = input('rock, paper or scissors? ')

# Here the logic is organized, based on the victory of the computer to define which will be
# the variable winner.    
if computer_choice == user_choice:
    winner = 'Tie'
elif computer_choice == 'paper' and user_choice == 'rock':
    winner = 'Computer'
elif computer_choice == 'rock' and user_choice == 'scissors' :
    winner = 'Computer'
elif computer_choice == 'scissors' and user_choice == 'paper' :
    winner = 'Computer'   
else:
    winner = 'User'   

# Announces tie or winner along with computer choice.
if winner == 'Tie':
    print('We both chose', computer_choice + ', play again.')
else :
    print(winner, 'won. The computer chose', computer_choice + '.')
