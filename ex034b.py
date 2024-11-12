salario = float(input('Qual é o salário do funcionário? R$'))
if salario <= 1250:
    novo = salario * 1.15
else:
    novo = salario * 1.10
print('Quem ganhava R${:.2f}, passa a ganhar agora R${:.2f}'.format(salario, novo))
