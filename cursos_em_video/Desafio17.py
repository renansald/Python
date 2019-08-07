from math import pow, sqrt, hypot
catOposto = float(input("Informe o cateto oposto: "))
catAdjacente = float(input("nforme o cateto adjacente: "))
print("A hipotenusa é igual a: {} ou  com hypot {}".format(sqrt((pow(catOposto, 2))+(pow(catAdjacente,2))), hypot(catOposto, catAdjacente)))
