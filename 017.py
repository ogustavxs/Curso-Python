import math
cato = float(input('Digite o comprimento do cateto oposto: '))
cata = float(input('Digite o comprimento do cateto adjascente: '))
print('A hipotenusa vai medir {:.2f}'.format(math.hypot(cato, cata)))