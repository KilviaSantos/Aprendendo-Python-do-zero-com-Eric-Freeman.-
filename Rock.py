import random

choices = ['rock', 'paper', 'scissors']
computer_choice = random.choice(choices)
user_choice = input('rock, paper or scissors?') 
print('You chose', user_choice, 'and the computer chose', computer_choice)        


