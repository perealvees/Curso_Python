#Faça um programa que leia do número 0 ao 1000 e que mostre na tela
#cada um dos digitos separados.

#exemplo numero 1834
# unidade 4, dezena 3, centena 8, milhar 1

num = int(input('Digite um número:'))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('Analisando o número {}:'.format(num))
print('Unidade {}'.format(u))
print('Dezena {}'.format(d))
print('Centena {}'.format(c))
print('Milhar {}'.format(m))
