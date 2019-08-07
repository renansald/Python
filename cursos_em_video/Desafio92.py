from datetime import date
profissional = dict();
profissional['Nome'] = str(input("Informe o nome da pessoa : ")).strip();
profissional['Nascimento'] = int(input("Ano de nascimento: "));
profissional['Idade'] = date.today().year - profissional['Nascimento'];
profissional['ctps'] = int(input("Informe o numero da carteira de trabalho (ctps): "));
if(profissional['ctps'] == 0):
    del profissional['ctps'];
else:
    profissional['Ano de contratação'] = int(input("Informe o ano da primeira contratação: "));
    profissional['Salário'] = float(input("Informe o salário: "));
    profissional['Idade de aposentadoria'] = 35 + (profissional['Ano de contratação'] - profissional['Nascimento']);
for k, v in profissional.items():
    print(f"{k}: {v}");
