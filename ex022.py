nome = str(input('Digite aqui seu nome completo: ')).strip()
print('Seu nome com letras maíusculas é {}'.format(nome.upper()))
print('Seu nome com letras minusculas é {}'.format(nome.lower()))
print('Seu nome sem espaços tem {} letras'.format(len(nome)-nome.count(' ')))
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e e ele tem {} letras'.format(separa[0],len(separa[0])))