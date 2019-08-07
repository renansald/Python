from random import shuffle

aluno1 = input('Informe o primeiro aluno: ')
aluno2 = input('Informe o segundo aluno: ')
aluno3 = input('Informe o terceiro aluno: ')
aluno4 = input('Informe o quarto aluno: ')
alunos = [aluno1, aluno2, aluno3, aluno4]
shuffle(alunos);
print('nova lista {}'.format(alunos))
