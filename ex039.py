from datetime import date
genero = str(input('Qual é o seu gênero? '))
nasci = int(input('Digite aqui o ano do seu nascimento: '))
ano = date.today().year
idade = ano - nasci
if genero == 'feminino':
    print('Você não precisa se alistar!')
elif idade <= 17:
    print('Você tem atualmente {} anos, ainda faltam {} ano(s) para você se alistar.'.format(idade, (18 - idade)))
    print('Você deve se alistar em {}.'.format(ano + (18 - idade)))
elif idade == 18:
    print('Você tem {} e está no prazo para se alistar.'.format(idade))
elif idade > 18:
    print('Você tem {} anos e já passou do prazo de alistamento em {} ano(s), é necessário realizar a regularização.'.format(idade, (idade - 18)))
    print('O alistamento devia ter sido realizado em {}'.format(ano - (idade-18)))
