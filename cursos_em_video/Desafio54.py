from datetime import date
count = 0
for x in range(0, 7):
    idade = int(input("Informe ano de nascimento da pessoa {}: ".format(x+1)))
    anoAtual = date.today().year
    if((anoAtual - idade) >= 18):
        count = count + 1
print("{} pessoas são maiores de idade".format(count))
