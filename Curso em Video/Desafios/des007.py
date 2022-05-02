# Faça um programa que leia duas notas de um aluno e retorne uma média.

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2) / 2

print('A primeira nota do aluno foi {} e a segunda nota foi {}. Sua média é: {}.'.format(n1, n2, m))