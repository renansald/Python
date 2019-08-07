nome1 = input("Informe um nome: ").strip()
nome = nome1.split()
print('O primeiro nome é {}\nO ultimo nome é {}'.format(nome[0], nome[len(nome)-1]))
print("{} {}".format(nome1[:nome1.find(' ')], nome1[nome1.rfind(' ')+1:]))
