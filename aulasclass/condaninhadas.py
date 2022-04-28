nome=str(input('Qual é o seu nome? '))
if nome=='Guilherme':
    print('Que nome bonito!')
elif nome== 'Pedro' or nome== 'Maria' or nome=='Paulo':
    print('Seu nome é bem popular no Brasil {}'.format(nome))
else:
    print('Tá')    
print('Tenha um bom dia {}'.format(nome))
