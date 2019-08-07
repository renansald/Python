salario = float(input('Informe o salário do comprador: '))
valorImovel = float(input('Informe o valor do imóvel: '))
nPrestacoes = int(input('Informe o número de prestações: '))
valorPrestacoes = valorImovel/nPrestacoes
if((salario*0.30) < valorPrestacoes):
    print("{}Infelizmente seu crédito não foi aprovado{}".format('\33[1;30;41m', '\33[m'))
else:
    print("Crédito aprovado")
