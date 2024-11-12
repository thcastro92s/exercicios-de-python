d = int(input('Quantos dias o carro ficou alugado? '))
k = float(input('Quantos kilometros o véiculo percorreu? '))
print('Seu véiculo ficou {} dias alugado e percorreu {} km, portanto é necessário realizar o pagamento de R$ {} '.format(d, k, ((d*60)+k*0.15)))
