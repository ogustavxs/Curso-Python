from random import shuffle
nomes = []
for _ in range(0, 4):
    nome = input('Digite o nome:')
    nomes.append(nome)
shuffle(nomes)
print('A ordem de apresentação será:', ', '.join(nomes))