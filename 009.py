num = int(input("Digite um numero para ver a tabuada: "))
print('----------')
for x in range(1, 11):
    print('{} + {} = {}'.format(num, x, num+x))
print('----------')