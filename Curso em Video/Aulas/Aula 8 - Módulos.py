#usando o import bebida o programa pega todos "itens" daquele conjunto

#usando o from "item" import, o programa pega apenas um item especifico

#importando a biblioeca Math, pode se usar alguns dos seguintes intens
#ceil (arredondar pra cima), floor (arredonda para baixo)
#trunc(deixa o número quebrado inteiro), pow(exponiação) sqrt (raiz quadrada), facotial (fatorial)


#import math
#num = int(input('Digite um número: '))
#raiz = math.sqrt(num)
#print('A raiz de {} é {:.2f}.'.format(num, raiz))

from math import sqrt
#nesse caso como ja estamos importando da boblioteca o sqrt, podemos chamar ela direto na variavel

num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de {} é {}.'.format(num, raiz))
