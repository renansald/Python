numero = int(input("Informe o termo da sequcnai de Fibonacci desejada: "));
n = 1;
ant = 0;
pos = 0;
while(pos < numero):
    print("{} ".format(n+ant), end="");
    aux = n;
    n += ant;
    ant = aux;
    pos += 1;
print();
