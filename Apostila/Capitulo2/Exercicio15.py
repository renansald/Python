salario = float(input("Informe o salário atual: "));
if(salario <= (750*1.5)):
    print(f"Novo salário é: {salario*1.30}");
else:
    print(f"Não tem aumento salario maior que {750*1.5}");
