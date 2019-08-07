times = ["Plameira", "Santos", "Flamengo", "Internacional", "Atletico Mineiro", "Goiás", "Botafogo", "Bahia", "São Paulo", "Corinthias", "Grêmio", "Athlitico-PR", "Ceará SC", "Fortaleza", "Vasco da Gama", "Fluminense", "Chapecoense", "Cruzeiro", "CSA", "Avaí",];
print(f"Os 5 primeiros colocados são {times[:5]}\nOs 4 ultimos colocados são {times[16:]}\nOs times participante são {sorted(times)}\n o Chapecoense está na {times.index('Chapecoense')+1}")

print("-"*30);
print("Os primeiros são: ");
for x in range(0, 5):
    print(times[x]);
print("-"*30);
print("Os quatro ultimos são: ");
for x in range(len(times) - 4, len(times)):
    print(times[x]);
print("*"*30);
print(f"Times participantes do campeonato em ordem alfabetica: {sorted(times)}");
print("^"*30)
print(f"A posição da Chapecoense é {times.index('Chapecoense') + 1}");
