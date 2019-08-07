nome = input('informe o nome: ').strip()
print('O nome em maiusculo é: {}\nO nome em minusculo é: {}\nO nome tem {} caracteres sem considera os \' \'\nO primeiro nome tem {} caracteres'.format(nome.upper(), nome.lower(), len(nome) - nome.count(' '), nome.find(" ")))
