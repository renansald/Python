def Notas(*notas, sit = False):
    """
    =>Avalia notas do aluno;
    :param notas: receiv n values of notes;
    :param sit: optional, show situation of the student;
    return: void;
    """
    notasd = dict();
    notasd['Total de notas'] = len(notas);
    notasd['Maior nota'] = max(notas);
    notasd['Menor nota'] = min(notas);
    notasd['Média'] = sum(notas)/len(notas);
    if(sit):
        if(notasd['Média'] > 7):
            notasd['Situação'] = "Boa";
        elif(6 <= notasd['Média'] <= 7):
            notasd['Situação'] = "Razoável";
        else:
            notasd["Média"] = "Ruim";
    for k, e in notasd.items():
        print(f"{k}: {e}");


###MAIN###
help(Notas);
Notas(8.5, 6.7, 9.9, sit=True);
Notas(1, 0, 1.1, sit=True);
