from Desafio107 import Moeda
moeda = float(input("Informe o valor: "));
print(f"Aumentando a moeda em 10% {Moeda.Aumentar(moeda, 10):.2f}");
print(f"Diminuindo a moeda em 60% {Moeda.Diminuir(moeda, 60)}");
print(f"Dobro {Moeda.Dobro(moeda)}");
print(f"Metade {Moeda.Metade(moeda)}");
