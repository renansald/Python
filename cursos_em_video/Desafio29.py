velocidade = float(input('Informe a velocidade: '))
if (velocidade > 80):
    acimaDoLimite = velocidade - 80
    multa = acimaDoLimite*7
    print("Multinha básica de R$ {:.2f}".format(multa))
