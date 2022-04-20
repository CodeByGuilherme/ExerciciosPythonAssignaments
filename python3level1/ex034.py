#DESAFIO 34:
#ESCREVA UM PROGRAMA QUE PERGUNTE O SALARIO DE UM FUNCIONÁRIO E CALCULE O VALOR DO SEU AUMENTO
#PARA SALÁRIOS SUPERIORES A R$1250,00, O AUMENTO É DE 10%
#PARA INFERIORES O AUMENTO É DE 15

salario = float(input('Valor do salário: R$'))
if salario<1250.00:
    aumento = salario/100*15
else:
    aumento = salario/100*10
print('Seu novo salário é de R${:.2f} !'.format(salario + aumento))

