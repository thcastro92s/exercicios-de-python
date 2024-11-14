nota1 = float(input('Digite aqui uma nota: '))
nota2 = float(input('Digite aqui outra nota: '))
media = (nota1 + nota2) / 2
if media < 5.0:
    print('Infelizmente sua média foi igual a {:.1f}, você foi reprovado'.format(media))
elif media >= 5 and media < 7:
    print('Sua média foi de {:.1f}, portanto você está de recuperação.'.format(media))
else:
    print('Sua média foi de {:.1f}. Parabéns você foi aprovado!'.format(media))
