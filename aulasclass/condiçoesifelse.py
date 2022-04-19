'''tempo = int(input('Quantos anos tem seu carro?'))
if tempo <=3:
    print('carro novo')
else:
    print('carro velho')
print('--FIM--')'''

#CONDIÇÃO SIMPLIFICADA
#pode se escrever a condição em apenas uma linha de comando:

'''tempo = int(input('Quantos anos tem seu carro?'))
print('carro novo' if tempo<=3 else 'carro velho')
print('--FM--')'''

'''nome = str(input('Qual é seu nome? '))
if nome == 'Guilherme':
    print('Olá usuário proprietário, acesso total concedido')
else:
    print('Seu nivel de usuario concede acesso limitado')
print('Bom dia, {}!'.format(nome))'''

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2)/2
print('A sua média foi {:.1f}'.format(media))
if media >= 6:
    print('Parabéns, você foi aprovado')
else:
    print('Você foi reprovado')



#DESAFIO 29:
#ESCREVA UM PROGRAMA QUE LEIA A VELOCDADE DE UM CARRO, SE ELE ULTRAPASSR 80KM/, MOSTRE UMA MENAGEM
#DIZENDO QUE ELE FOI MULTADO.
#A MULTA VAI CUSTAR R$7,00 POR CADA KM ACIMA DO LIMITE
#DESAFIO 30:
#CRIE UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO E MOSTRE NA TELA SE ELE É PAR OU IMPAR
#DESAFIO 31:
#DESENVOLVA UM PROGRAMA QUE PERGUNTE A DISTANCIA DE UMA VIAJEM EM KM, CALCULE O PREÇO DA PASSAGEM
#COBRANDO R$0,50 POR KM PARA VIAGENS ATÉ 200KM E R$0,45 PARA VIAGENS MAIS LONGAS
#DESAFIO 32:
#FAÇA UM PROGRAMA QUE LEIA UM ANO QUALQUER E MOSTRE SE ELE É  BISSEXTO
#DESAFIO 33:
#FAÇA UM PROGRAMA QUE LEIA TRÊS NUMEROS E MOSTRE QUAL É O MAIOR E QUAL O MENOR.
#DESAFIO 34:
#ESCREVA UM PROGRAMA QUE PERGUNTE O SALARIO DE UM FUNCIONÁRIO E CALCULE O VALOR DO SEU AUMENTO
#PARA SALÁRIOS SUPERIORES A R$1250,00, O AUMENTO É DE 10%
#PARA INFERIORES O AUMENTO É DE 15%
#DESAFIO 35:
# DESENVOLVA UM PROGRAMA QUE LEIA O COMPRIMENTO DE TRÊS RETAS 
#  DIGA AO USUÁRIO SE ELAS PODEM OU NÃO FORMAR UM TRIÃNGULO.
