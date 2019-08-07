numeros = ["zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "catoze", "quize", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte"];
numero = int(input("Digite um número: "));
while((numero > 20) or (numero < 0)):
    numero = int(input("Erro, por favor digite um novo número entre 0 e 20: "));
print(f"O numero {numero} em extenso corresponde a {numeros[numero]}");
