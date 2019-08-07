from datetime import date
def Voto(ano = 0):
    """
    :param ano: Reciver the year of born;
    :return : void;
    """
    idade = (date.today().year - ano);
    if ano == 0 or ano > date.today().year:
        return("Ano inválido");
    elif((16 <= idade < 18) or (idade >= 65)):
        return(f"Com {idade} anos o voto opcional!!!!");
    elif(idade < 16):
        return(f"Com {idade} anos não vota ainda");
    else:
        return(f"Com {idade} anos o voto é obrigatório");


###Main###
print("_-"*30);
print(Voto(1993));
print(Voto(2003));
print(Voto(2002));
print(Voto(2001));
print(Voto(1955));
str = Voto(1940);
str1 = Voto(2012);
print(str);
print(str1);
