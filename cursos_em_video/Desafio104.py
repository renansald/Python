def LeiaInt(msg):
    while True:
        try:
            num = int(input(msg));
            return num;
        except Exception as e:
            print(f"Deve ser um inteiro{e}");


###Main###
num = LeiaInt("Int idiota: ");
print(num);
