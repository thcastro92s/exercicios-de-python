n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
if n1 > n2:
    print('O número {} é maior que o segundo número {} digitado'.format(n1, n2))
elif n2 > n1:
    print('O número {} digitado é maior que o primeiro número {} digitado.'.format(n2, n1))
elif n1 == n2:
    print('Foi digitado o número {} e o número {}, portanto os dois valores são iguais'.format(n1, n2))
