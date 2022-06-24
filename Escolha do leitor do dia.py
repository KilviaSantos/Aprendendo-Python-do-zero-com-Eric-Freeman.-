import random
print ('Leitor do dia')
lista_pessoas = ['Abraão', 'Kilvia', 'Fabíola', 'Sophia', 'Sarah']
lista_livros = ['Eu de cabeça para baixo', 'Bíblia de adulto', 'Bíblia infantil', 'Frozen', 'O dever da esperança']

pessoa = random.choice(lista_pessoas)
livro = random.choice(lista_livros)

print('O leitor de hoje é ' +  pessoa + ', que vai ler o livro: '+ livro)
