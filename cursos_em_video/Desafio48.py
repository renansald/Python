soma = 0
for x in range(1, 501):
    if(((x%2) != 0) and ((x%3) == 0)):
        soma +=x
print(soma)
