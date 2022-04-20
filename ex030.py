#DESAFIO 30:
#CRIE UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO E MOSTRE NA TELA SE ELE É PAR OU IMPAR

n1 = float(input('Digite um número: '))
res = n1 % 2
if res == 0:
    print('O número é par')
else:
    print('O número é impar')

