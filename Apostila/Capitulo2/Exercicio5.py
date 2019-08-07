num = float(input("Informe o número: "));
num2 = float(input("Informe o segundo número: "));
num3 = float(input("Informe o terceiro número: "));
if((num > num2) and (num > num3)):
    print(f"O maior número é {num:.2f}");
elif((num2 > num) and (num2 > num3)):
    print(f"O maior número é {num2:.2f}");
elif((num3 > num) and (num3 > num2)):
    print(f"O maior número é {num3:.2f}");
elif((num == num2) and (num > num3)):
    print(f"O maior numero é {num:.2f}");
elif((num == num3) and (num > num2)):
    print(f"O maior número é {num:.2f}");
elif((num2 == num3) and (num2 > num)):
    print(f"O maior número é {num2:.2f}");
else:
    print("São todos iguais");
