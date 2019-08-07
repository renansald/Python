pagamento = int(input("Escolha a forma de pagemnto:\nDigite 1 para pagemtno a vista no dinheiro/cheque\nDigite 2 para pagamento a vista no crédito\nDigite 3 para pagamento em até 2x no cartão\nDigite 4 para pagamentos acima de 2x no cartão: "))
preco = float(input("Valor a ser pago: "))
if(pagamento == 1):
    print("Valor a ser pago: {}".format(preco - 0.10*preco))
elif(pagamento == 2):
    print("Valor a ser pago: {}".format(preco - 0.05*preco))
elif(pagamento ==3):
    print("Valor a ser pago: {}".format(preco));
else:
    print("Valor a ser pago: {}".format(preco*1.20))
