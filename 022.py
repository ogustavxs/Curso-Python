import time
nome = input('Digite seu nome completo: ').strip()
time.sleep(1)
print('Analisando seu nome...')
time.sleep(1.5)
print('Seu nome em maiúsculas é: {}'.format(nome.upper()))
print('Seu nome em minúsculas é: {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
print('Seu primeiro nome é {} e ele tem {} letras'.format(nome[0], len(nome[0])))