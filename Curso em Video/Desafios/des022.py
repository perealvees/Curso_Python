#Crie um programa que leia o nome da pessoa e mostre:
#O nome com todas as letras maiúsuclas
#o nome com todas minúsculas
#Quantas letras no total sem contar espaços
#Quantas letras tem o primeiro nome

nome = str(input('Qual é o seu nome completo?')).strip()
print('Analisando seu nome')
print('Seu nome em maiúsculo fica {}'.format (nome.upper()))
print('Seu nome em minúsculo fica {}:'.format(nome.lower()))
print('Seu nome contém total de {} letras'.format(len(nome)-nome.count(' ')))
print('Seu primeiro nome {} letras'.format(nome.find(' ')))
