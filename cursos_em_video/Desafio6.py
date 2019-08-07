numero = int(input("Informe um número: "));
print("O numero {:*>30} tem como dobro {:-^5}, como triplo {:_<6} e raiz quadrada {:.2f}".format(numero, numero*2, numero*3, numero**(1/2)))
