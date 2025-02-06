import random

numero = (random.randint(1, 10))

while True:
    arvaus=input("Arvaa numero: ")
    print(numero)
    if int(arvaus) > int(numero):
        print("Liian suuri numero")
    elif int(arvaus) < int(numero):
        print("Liian pieni numero")
        input("Arvaa numero: ")
    elif int(arvaus)==int(numero):
        print("Oikein")


