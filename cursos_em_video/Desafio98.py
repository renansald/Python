def Contador(inicio, fim ,passo):
    if(passo < 0):
        pas = passo * (-1)
    elif(passo == 0):
        pas = 1;
    else:
        pas = passo;
    print(f"Contagem de {inicio} a {fim} de {pas} em {pas}");
    if(inicio < fim):
        cont = inicio;
        while(cont <= fim):
            print(f"{cont}", end=" ");
            cont += pas;
        print("FIM!!");
    else:
        cont = inicio;
        while(cont >= fim):
            print(f"{cont}", end=" ");
            cont -= pas;
        print("FIM!");

###MAIN###
print("-="*30);
print("Contagem de 1 a 10 de 1 em 1");
Contador(1, 10, 1);
print("-="*30);
print("Contagem de 10 até 0 de 2 em 2");
Contador(10, 0, 2);
print("-="*30);
print("Contagem personalizada");
inicio = int(input("Início: "));
fim = int(input("Fim: "));
passo = int(input("Passo: "));
Contador(inicio, fim, passo);
