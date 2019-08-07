sexo = ''
while ((sexo != 'M') and (sexo != 'F')):
    sexo = str(input("Informe o sexo: "))
    if((sexo != 'M') and (sexo != 'F')):
        print("o sexo deve ser M para masculino e F para feminino.", end = " ")
print(sexo)
