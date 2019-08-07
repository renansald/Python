nome = str(input("Informe o nome: ")).strip();
peso = float(input("Informe o peso da pessoa: "));
idade = int(input("Informe a idade da pessoa: "));
if(((idade >= 18) and (idade <= 67)) and (peso > 50)):
    print(f"\33[1;32;40m{nome} pode ser doador de sangue\33[m");
else:
    print(f"\33[1;31m{nome} não pode ser doador de sangue\33[m");
