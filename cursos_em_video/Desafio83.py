lista = list();
expressao = str(input("Informe a expressão: "));
for letra in expressao:
    if(letra == "("):
        lista.append(letra);
    elif((letra == ")") and (len(lista) > 0)):
        lista.pop();
    elif(letra == ")"):
        lista.append(")");
        break;  
if(len(lista) == 0):
    print("\33[2;32m Expressão correta\33[m");
else:
    print("\33[2;31m Expressão incorreta\33[m");
