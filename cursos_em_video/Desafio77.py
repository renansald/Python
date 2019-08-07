palavras = ["Renan", "python", "Computação", "Vida", "ignição", "engenharia"];
for palavra in palavras:
    print(f"A palavra {palavra} tem:", end=" ");
    for letra in palavra:
        if letra.lower() in 'aeiouáãêõü':
            print(f"{letra}", end = " ");
    print("");
