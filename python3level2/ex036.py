'''
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo  que ela não pode exceder 30% salário,
ou então, o empréstimo será negado.
'''

salvalor = float(input('Digite o salário do solicitante: '))
imovelvalor = float(input('Digite o valor do imóvel: '))
anosfinanc = int(input('Digite em quantos anos vocẽ pretende financiar: '))
parcelavalor = imovelvalor/anosfinanc/12
print('o valor da sua parcelá sairá : {:.2f}'.format(parcelavalor))
tetoparcel  = salvalor/100*30
if parcelavalor<=tetoparcel:
    print('O empréstimo foi aprovado')
else:
    print('O empréstimo foi negado')


