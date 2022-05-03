# Ler o preço de um produto e adicionar mais 5% de desconto

p = float(input('Qual o valor do produto? R$ '))
novo = p - (p * 5 / 100)
print('O produto  é R${:.2f} mas a vista tem um desconto de 5% e fica {:.2f} R$.'.format(p, novo))