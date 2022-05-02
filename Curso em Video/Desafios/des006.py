# Faça um programa que leia um número e que mostre seu dobro, triplo e a raiz quadrada

n = int(input('Digite um número: '))
d = n * 2
t = n * 3
r = n ** (1/2)

print('O número diitado foi: {} \no dobro é: {} \no triplo é: {} \ne sua raiz quadrada é: {:.2f}.'.format(n, d, t,r))