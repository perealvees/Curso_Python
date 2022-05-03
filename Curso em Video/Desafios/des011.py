# Ler a altura e largura de uma parede em metros, calcular area e a quantidade
# de tinta necessária para pinta-lá, sabendo que cada litro de tinta pinta 2m²

l = float(input('Qual é a largura da sua parede? '))
a = float(input('Qual a altura da sua parede? '))
t = l * a
print('Sua parede tem dimensão de {}  x {} e sua area total é {}m².'.format(l, a, t))
tinta = t / 2
print('Para pintar {}m², você precisará de {} litros de tinta.'.format(t, tinta))