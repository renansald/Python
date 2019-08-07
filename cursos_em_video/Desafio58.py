from random import randint
numero = randint(0, 10)
player = int(input("Tente advinhar o que eu pensei: "))
count = 1
while(player != numero):
    count += 1
    player = int(input("Você errou tente advinhar novamente o que eu pensei: "))
if(count == 1):
    print("Você é o mestre da adivinhação consegue com {} tentativas".format(count))
elif((count > 1) and (count <= 5)):
    print("Você esta na média conssguiu com {} tentativas".format(count))
else:
    print("Você é só mais um")
