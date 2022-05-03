# Escreva um programa para ler o valor em metros e exibir convertido em centímetros e milímetros

m = float(input('Qaul a distancia que deseja calcular em metros?'))
cem = m * 100
mil = m *1000
print('{} em centimentro fica {:.0f} centímetros e em milimetros fica {:.0f} .'.format(m, cem, mil))