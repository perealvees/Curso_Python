#Ordem de precedência dos operadores:
#1º ()
#2º **
#3º * / // %
#4º +-

#- - - - - -
#usar o {:^20} para ter um total de x caractere

#nome = input('Olá, qual é o seu nome? ')
#print('Seja bem vindo(a) {:=^20}'.format(nome))
#- - - - - - -

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

#print('A soma é {}, o produto é {} e a divisão é {:.3f}.'.format(s, m, d))
#print('A divisão inteira {} e a potencia {}'.format(di, e))

#para juntar duas impressões usar o " end=' ' "
#print('A soma é {}, o produto é {} e a divisão é {:.3f}.'.format(s, m, d), end=' ')
#print('A divisão inteira {} e a potencia {}'.format(di, e))

#para quebrar a linha usar o " \n"
print('A soma é {}, o produto é {} \n e a divisão é {:.3f}.'.format(s, m, d), end=' ')
print('A divisão inteira {} e a potencia {}'.format(di, e))

