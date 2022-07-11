import random
# Importa o módulo random.
winner = ''
# Configura a variável winner.

choices = ['rock', 'paper', 'scissors']
computer_choice = random.choice(choices)
# O computador escolhe aleatoriamente pedra, papel ou tesoura através do 
# random.choice.

user_choice = ''
while (user_choice != 'rock' and 
        user_choice != 'paper' and
        user_choice != 'scissors') :
    user_choice = input('rock, paper or scissors? ')
# Identifica se o usuário fez uma escolha inválida e o while solicicita novamente
# até que seja uma entrada válida.        

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
# Aqui é organzada a lógica, baseada na vitória do computadr para definir qual será
# a variável winner.

if winner == 'Tie':
    print('We both chose', computer_choice + ', play again.')
else :
    print(winner, 'won. The computer chose', computer_choice + '.')
# Anuncia o empate ou o vencedor junto com a escolha do computador.
