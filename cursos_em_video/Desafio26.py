frase = input('Informe uma frase: ').strip()
print("A frase possui {} \'A\'\nO primeiro a aparece na posição {} e o ultimo a aparece na posição {}".format(frase.lower().count('a'), frase.lower().find('a'), frase.upper().rfind('A')))
