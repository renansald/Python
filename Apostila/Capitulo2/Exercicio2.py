num1 = float(input("Informe o primeiro número: "));
num2 = float(input("Informe o segundo número: "));
num3 = float(input("Informe o terceiro número: "));
if((num1 >= num2) and (num2 >= num3)):
    print(f"{num1:.2f}, {num2:.2f}, {num3:.2f}");
elif((num1 >= num3) and (num3 >= num2)):
    print(f"{num1:.2f}, {num3:.2f}, {num2:.2f}");
elif((num2 >= num1) and (num1 >= num3)):
    print(f"{num2:.2f}, {num1:.2f}, {num3:.2f}");
elif((num2 >= num3) and (num3 >= num1)):
    print(f"{num2:.2f}, {num3:.2f}, {num1:.2f}");
elif((num3 >= num1) and (num1 > num2)):
    print(f"{num3:.2f}, {num1:.2f}, {num2:.2f}");
elif((num3 >= num2) and (num2 >= num1)):
    print(f"{num3:.2f}, {num2:.2f}, {num1:.2f}");
