from datetime import date
nasci = int(input('Digite aqui o ano de seu nascimento: '))
idade = date.today().year - nasci
if idade <= 9:
    print('Você tem atualmente {} anos, e está na categoria MIRIM.'.format(idade))
elif idade <= 14:
    print('Você tem atualmente {} anos, e está na categoria INFANTIL'.format(idade))
elif idade <= 19:
    print('Você tem atualmente {} anos, e está na categoria JUNIOR'.format(idade))
elif idade == 20:
    print('Você tem atualmente {} anos, e está na categoria SÊNIOR'.format(idade))
else:
    print('Você tem atualmente {} anos, e está na categoria MASTER'.format(idade))
