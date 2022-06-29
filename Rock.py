import random

winner = ''
choices = ['rock', 'paper', 'scissors']
computer_choice = random.choice(choices)
user_choice = input('rock, paper or scissors? ')       

if computer_choice == user_choice:
    winner = 'Tie'

