preço = float(input('Digite o preço do produto: R$'))
desconto = preço*0.05
print('Com 5% de desconto você economiza R${:.2f}, e paga somente R${:.2f}!'.format(desconto, preço-desconto))