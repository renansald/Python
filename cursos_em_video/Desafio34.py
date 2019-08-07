salario = float(input('Informe o Salário do funcionário: '))
if(salario > 1250):
    print("O novo salario é {:.2f}".format(salario*1.10))
else:
    print("O novo salario é {:.2f}".format(salario*1.15))
