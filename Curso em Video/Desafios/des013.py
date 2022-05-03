# Ler um salário e adicionar mais 15% de aumento

sal = float(input('Qual o valor do seu salário R$? '))
salt  = sal + (sal  * 15/100)
input('Seu salário teve um aumento de 15% e agora é {} R$ '.format(salt))