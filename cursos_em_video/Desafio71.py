valor = int(input("Informe o valor que deseja sacar: "));
numero50 = valor//50;
resto = valor%50;
numero20 = resto//20;
resto = valor%20;
numero10 = resto//10;
resto = valor%10;
numero1 = resto//1;
print(f"São {numero50} cedulas de R$ 50\nSão {numero20} cedulas de 20\nSão {numero10} cedulas de 10\nSão {numero1} cedulas de 1")
