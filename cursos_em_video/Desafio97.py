def Escrita(msg):
    tamanho = len(msg) + 4;
    print(("~" * tamanho)+f"\n  {msg}\n"+("~" * tamanho));

###Main###
Escrita("Olá mundo!");
Escrita("Hoje a jiripoca will piu piu");
