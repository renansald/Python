idadeAnt = 0
somador = 0
nWomen = 0
oldMan = ""
for x in range(1, 5):
    nome = str(input('Informe o nome da {}ª pessoa: '.format(x)))
    sexo = str(input("Informe o sexo da {}ª pessoa: ".format(x))).upper()
    idade = int(input("Infomre a idade da {}ª pessoa: ".format(x)))
    somador = somador + idade
    if((sexo == "M") and (idade > idadeAnt)):
        oldMan = nome
        idadeAnt = idade
    if((sexo == "F") and (idade < 20)):
        nWomen = nWomen + 1;
if(oldMan != ""):
    print(""" A média de idade é {}
    O homem mais velho é {}
    O númeor de mulheres com idade inferior a 20 anos é {}""".format(somador/4, oldMan, nWomen))
else:
    print(""" A média de idade é {}
    Não temos homens no grupo
    O númeor de mulheres com idade inferior a 20 anos é {}""".format(somador/4, nWomen))
