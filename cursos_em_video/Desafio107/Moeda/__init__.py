def Metade(moeda = 0):
    return moeda/2;

def Aumentar(moeda = 0, porcentagem = 0):
    return moeda * (1 + (porcentagem/100));

def Dobro(moeda = 0):
    return moeda*2;

def Diminuir(moeda = 0, porcentagem = 0):
    return moeda*(1 - porcentagem/100);
