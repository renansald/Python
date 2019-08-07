import datetime
anoNascimento = int(input("Informe o seu ano de nascimento: "))
anoAtual = datetime.date.today()
if((anoAtual.year - anoNascimento) == 18):
    print("Hora de alistar")
elif((anoAtual.year - anoNascimento) < 18):
    print("Ainda faltam {} anos para se alistar",format((18 - (anoAtual.year - anoNascimento))))
else:
    print("\33[7;30;41m Já passou da hora de se alistar, vc está a {} atrasado\33[m".format((anoAtual.year - anoNascimento) - 18))
