numero = list();
while (True):
    num = float(input("Informe um valor: "));
    if num in numero:
        print("O valor já foi adicionado anteriormente");
    else:
        numero.append(num);
        print("Valor adicionado com sucesso");
    opt = str(input("Deseja continuar/ [S/N]: ")).strip().upper();
    while((opt != 'S') and (opt != 'N')):
         opt = str(input("Informe apenas os caracteres solicitidos. Deseja continuar/ [S/N]: ")).strip().upper();
    if opt == 'N':
        break;
numero.sort();
for n in numero:
    print(f"{n:.2f}", end = " ");
print("")
