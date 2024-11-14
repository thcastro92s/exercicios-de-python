peso = float(input('Digite aqui o seu peso: '))
altura = float(input('Digite aqui a sua altura: '))
imc = peso / altura ** 2
if imc < 18.5:
    print('Seu IMC está no valor de {:.1f}kg/m², portanto você está abaixo do peso'.format(imc))
elif 18.5 <= imc < 25:
    print('Seu IMC está no valor de {:.1f}kg/m², portanto você está no peso ideal'.format(imc))
elif 25 <= imc < 30:
    print('Seu IMC está no valor de {:.1f}kg/m², portanto você está em sobrepeso'.format(imc))
elif 30 <= imc < 40:
    print('Seu IMC está no valor de {:.1f}kg/m², portanto você está obeso.'.format(imc))
else:
    print('Seu IMC está no valor de {:.1f}kg/m², portanto você está em obesidade mórbida'.format(imc))
