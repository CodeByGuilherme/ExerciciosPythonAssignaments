#DESAFIO 28:
#ESCREVA UM PROGRAMA QUE FAÇA O COMPUTADOR PENSAR EM UM NUMERO INTEIRO  E 0 5 E PEÇA PARA O USUARIO
#DESCOBRIR QUAL FOI O NÚMERO ESCOLHIDO PELO COMPUTADOR, O PROGRAMA DEVERÁ DIZER
#SE O USUÁRIO VENCEU OU PERDEU.
 
 
from random import randint
machine = randint(0,5)
usuario = int(input('Te desafio a adivinhar o número que pensei! digite um número: '))
if usuario==machine:
    print('Parabéns, você acertou!!!')
else:
    print('Você falhou, o número é {}'.format(machine))
    



