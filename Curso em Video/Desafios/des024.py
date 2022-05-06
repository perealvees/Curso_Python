#Crie um programa que leia o nome de uma cidade e diga se ela começa com Santo ou não
cid = str(input('Digite uma cidade:')).strip()
print(cid[:5].upper() == 'SANTO')
