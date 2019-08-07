countIdade = nHomens = nMulheres = 0;
while(True):
    idade = int(input("Informe a idade: "));
    while(True):
        sexo = str(input("Informe o sexo da pessoa[M/F]")).strip().upper();
        if((sexo == 'M') or (sexo =='F')):
            break;
    if(idade > 18):
        countIdade += 1;
    if(sexo == 'M'):
        nHomens += 1;
    if((sexo == 'F') and (idade < 20)):
        nMulheres += 1;
    while(True):
        opcao = str(input("Deseja efetuar um novo cadastro[S/N]: ")).strip().upper();
        if((opcao == "S") or (opcao == "N")):
            break;
    if(opcao == 'N'):
        break;
print(f"Foram cadastrada {countIdade} com mais de 18 anos\nForam cadastrado {nHomens} homens\nForam cadastradas {nMulheres} com menos de 20 anos")
