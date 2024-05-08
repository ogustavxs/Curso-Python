salario = float(input('Qual é o salário do funcionario: R$'))
aumento = salario*0.15
print('Agora seu salario de R${:.2f} ganhará um aumento de R${:.2f}, e passara a ser de R${:.2f}!'.format(salario, aumento, salario+aumento))