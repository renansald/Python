distancia = float(input("Informe a distância em Km da viagem: "))
if(distancia <= 200):
    print('O preço da passagem é {}'.format(distancia*0.50))
else:
    print('O preço da passagem é {}'.format(distancia*0.45))
