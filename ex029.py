#DESAFIO 29:
#ESCREVA UM PROGRAMA QUE LEIA A VELOCDADE DE UM CARRO, SE ELE ULTRAPASSR 80KM/h, MOSTRE UMA MENAGEM
#DIZENDO QUE ELE FOI MULTADO.
#A MULTA VAI CUSTAR R$7,00 POR CADA KM ACIMA DO LIMITE

vel = float(input('Qual a velocidade do veículo? '))
excedente = vel-80
multa = excedente*7
if vel > 80:
    print('Você excedeu o limite da via em {} km, sua multa é de R${:.2f}.'.format(excedente, multa))
else:
    print('Velocidade dentro do limite')
