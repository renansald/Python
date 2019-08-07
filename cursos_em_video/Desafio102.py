from time import sleep
def Fatorial(numero, show = False):
    f = 1;
    if(show):
        for x in range(numero, 0, -1):
            f = f*x;
            print(f"{x}", end="x", flush = True);
            sleep(0.5);
        print(f);
    else:
        for x in range(numero, 0, -1):
            f = f*x;
        print(f);


###Main###
Fatorial(5);
Fatorial(5, True);
Fatorial(5, False);
