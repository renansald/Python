def CalculaArea(comprimento, largura):
    print(f"A área do terreno de {comprimento} x {largura} é: {largura*comprimento}m²");

###Main###
comprimento = float(input("Informe o comprimento do terreno: "));
largura = float(input("Informe a largura do terreno: "));
CalculaArea(comprimento, largura);
