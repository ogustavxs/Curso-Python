import random
nomes = []
for _ in range(0, 4):
    nome = input('Digite o nome:')
    nomes.append(nome)
print('O aluno escolhido foi: {}'.format(random.choice(nomes)))