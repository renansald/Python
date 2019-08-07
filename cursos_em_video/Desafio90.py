aluno = dict();
aluno['Nome'] = str(input("Informe o nome do aluno: ")).strip();
aluno['Média'] = float(input("Informe a média desse aluno: "));
while((aluno['Média'] > 10) or (aluno['Média'] < 0)):
    aluno['Média'] = float(input("\33[1;31mERRO: média fora do intervalo de 0 a 10\33[m\nInforme a média desse aluno: "));
if(aluno['Média'] >= 7):
    aluno["Situação"] = "\33[1;32mAPROVADO";
else:
    aluno["Situação"] = "\33[1;31mREPROVADO";
print(f"Nome: {aluno['Nome']}\nMédia: {aluno['Média']}\nSituação: {aluno['Situação']}")
