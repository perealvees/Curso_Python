#usando o import bebida o programa pega todos "itens" daquele conjunto

#usando o from "item" import, o programa pega apenas um item especifico

#importando a biblioeca Math, pode se usar alguns dos seguintes intens
#ceil (arredondar pra cima), floor (arredonda para baixo)
#trunc(deixa o número quebrado inteiro), pow(exponiação) sqrt (raiz quadrada), facotial (fatorial)

import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é {:.1f}.'.format(num, raiz))