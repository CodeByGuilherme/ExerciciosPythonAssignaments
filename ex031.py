#DESAFIO 31:
#DESENVOLVA UM PROGRAMA QUE PERGUNTE A DISTANCIA DE UMA VIAJEM EM KM, CALCULE O PREÇO DA PASSAGEM
#COBRANDO R$0,50 POR KM PARA VIAGENS ATÉ 200KM E R$0,45 PARA VIAGENS MAIS LONGAS

distancia = float(input('Qual a distancia da viagem? '))
if distancia <= 200:
    print('O valor de sua passagem é: R${:.2f}'.format(distancia*0.50))
else:
    print('O valor de sua passagem é: R${:.2f}'.format(distancia*0.45))
print('Boa viagem!!!')
