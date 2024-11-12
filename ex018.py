from math import radians, sin, cos, tan
angulo = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('O valor de {} é SENO de {:.2f} '.format(angulo, seno))
print('O valor de {} é COSSENO de {:.2f} '.format(angulo, cosseno))
print('O valor de {} é TANGENTE de {:.2f} '.format(angulo, tangente))
