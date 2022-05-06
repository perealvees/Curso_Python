#Fatiamento de string
#Quando se tem uma range, começa a contagem pelo 0 e se remove o ultimo.

frase = 'Curso em Video Python!'

#print(frase)

#print(frase[3:13]) #da 3ª a 13ª

#print(frase[1:10:2])  #do 1ª ao 10 ª em 2 em 2.

#print(""""O texto dissertativo-argumentativo é um gênero discursivo \nmuito comum em provas de vestibular, como a Fuvest, e no Enem. Em resumo, trata-se de \numa produção em que um autor defende seu ponto de vista por meio de argumentos. \nNo caso específico do Exame Nacional do Ensino Médio, exige-se, também, que se apresentem """)

#print(len(frase))

#print(frase.split())
#print(frase.replace('Python', 'Maravilhoso'))
#print('Curso' in frase )
print(frase.lower().find('video'))

