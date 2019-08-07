import time
numero1 = float(input("Informe o primeiro valor: "))
numero2 = float(input("Informe o segundo valor: "))
opcao = 0
while(opcao != 5):
    opcao = int(input("""[1]Somar
[2]Multiplicar
[3]Maior
[4]Novos Números
[5]Sair do programa
Escolha uma das opções acima: """))
    if(opcao == 1):
        print("A soma entre {:.2f} e {:.2f} é {:.2f}".format(numero1, numero2, numero1+numero2))
        time.sleep(1)
    elif(opcao == 2):
        print("A multiplicação entre {:.2f} e {:.2f} é {:.2f}".format(numero1, numero2, numero1*numero2))
        time.sleep(1)
    elif(opcao == 3):
        print("O maior valor é {:.2f}".format(numero1 if numero1 >= numero2 else numero2))
        time.sleep(1)
    elif(opcao == 4):
        numero1 = float(input("Informe o primeiro número: "))
        numero2 = float(input("Informe o segundo número: "))
        time.sleep(1)
    elif(opcao == 5):
        print("Obrigado por ussar a nossa aplicação")
        break
    else:
        print("Opção inválida")
        time.sleep(1)
