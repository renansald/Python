cidade = input("informe o nome da cidade: ").strip()
cidade2 = cidade.split();
if  'SANTO' == cidade2[0].upper():
    print("Existe santo")
else:
    print('Não existe Santo')

#Outro metodo
print("santo" == cidade[:5].lower())
