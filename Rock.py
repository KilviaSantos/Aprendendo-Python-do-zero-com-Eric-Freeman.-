import random

random_choice = random.randint(0,2)
print('The computer chooses', random_choice)
if random_choice==0:
    print('rock')
elif random_choice==1:
    print('paper')
else:
    print('scissors')


#se random_choice==0, computer_choice=='rock'
#se random_choice==1, computer_choice=='paper'
#se random_choice==2, computer_choice=='scissors'

