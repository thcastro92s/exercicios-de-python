vcasa = float(input('Qual o valor da casa que você deseja comprar? R$ '))
salario = float(input('Qual o valor do seu salário? R$ '))
anos = int(input('Quantos anos você deseja pagar a casa? '))
prestacao = vcasa / (anos * 12)
print('O valor da prestação será de R${:.2f}'.format(prestacao))
if prestacao >= salario * 0.30:
    print('Infelizmente, seu empréstimo foi negado, por isso não é possível prosseguir com a compra.')
else:
    print('Parabéns! Seu empréstimo foi aprovado!')
