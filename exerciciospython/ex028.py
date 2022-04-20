#DESAFIO 28:
#ESCREVA UM PROGRAMA QUE FAÇA O COMPUTADOR PENSAR EM UM NUMERO INTEIRO  E 0 5 E PEÇA PARA O USUARIO
#DESCOBRIR QUAL FOI O NÚMERO ESCOLHIDO PELO COMPUTADOR, O PROGRAMA DEVERÁ DIZER
#SE O USUÁRIO VENCEU OU PERDEU.
 
 
from random import randint
from time import sleep #adicionei para dar uma atmosfera de jogo
machine = randint(0,5)
usuario = int(input('Te desafio a adivinhar o número que pensei! digite um número: '))
print('processando')
sleep(2)#essa funcionalidade suspende por uns segundos, dando a impressão que o computador está pensado
if usuario==machine:
    print('Parabéns, você acertou!!!')
else:
    print('Você falhou, o número é {}'.format(machine))





