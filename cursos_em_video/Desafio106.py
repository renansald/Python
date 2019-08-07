def Ajuda(comando):
    if comando == None:
        print("Deve ser informando um comando");
        return;
    else:
        msg1 = "Sistema de ajudas pyHelp";
        print("\33[1;34m");
        print("~"*(len(msg1)+4));
        print("  "+msg1);
        print("~"*(len(msg1)+4));
        print("\33[m");
        msg2 = "Acessando manual do "+comando;
        print("\33[1;32m");
        print("~"*(len(msg2)+4));
        print("  "+msg2);
        print("~"*(len(msg2)+4));
        print("\33[m")
        help(comando);


###MAIN###
while True:
    v = str(input("Informe o comando desejado: ")).strip().lower();
    if(v == "fim"):
        break;
    else:
        Ajuda(v);
