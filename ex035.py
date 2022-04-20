#DESAFIO 35:
#DESENVOLVA UM PROGRAMA QUE LEIA O COMPRIMENTO DE TRÊS RETAS 
#DIGA AO USUÁRIO SE ELAS PODEM OU NÃO FORMAR UM TRIÃNGULO.

r1 = float(input('Reta 1: '))
r2 = float(input('Reta 2: '))
r3 = float(input('Reta 3: '))
if r1 < r2+r3:
    true=r1
if r2 < r1+r3:
    true=r2
if r3 < r1+r2:
    true=r3  
if r1==true and r2==true and r3==true:
    print('As retas indicadas formam um triângulo.')   
else:
    print('Não foi possível formar um triângulo.') 
