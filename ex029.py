velocidade = float(input('Qual a velocidade do seu carro neste momento: '))
print('Sua velocidade foi de {} Km'.format(velocidade))
if velocidade > 80:
    print('Você ficou acima da velocidade máxima permitida, será necessário o pagamento de R$ {:.2f}'.format((velocidade - 80)*7))
print('Sua velocidade ficou dentro do limite permitido tenha uma boa viagem!')
