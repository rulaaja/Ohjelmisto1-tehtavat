

parilliset=[]
lista=[]

def lasku(lista):
    while True:
        luku2=int(input("Anna numero, painta enter lopettaaksesi: "))
        if luku2 == "": break
        lista.append(luku2)


for luku in lista:
    if luku % 2 == 0:
        parilliset.append(luku)
        print(f"Lista ilman parittomia lukuja on {parilliset} ja alkuperäinen lista on {lista}")



lasku(lista)

