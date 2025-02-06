lista=[]
while True:
    luku=input("Syötä luku: ")
    if luku =="":
        break
    lista.append(int(luku))
if lista:
    print(f"{min(lista)} on pienin luvuista ja {max(lista)} on suurin")

