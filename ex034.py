salario = float(input('Digite aqui o valor do seu salário:R$ '))
if salario > 1250:
    print('Seu salário está no valor de R${:.2f}, portanto o novo valor será de R${:.2f}'.format(salario, (salario * 1.10)))
else:
    print('Seu salário está no valor de R${:.2f}, e portanto o novo valor será de R${:.2f}'.format(salario, (salario * 1.15)))
