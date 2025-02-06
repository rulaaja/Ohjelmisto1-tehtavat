luku=input("Anna luku: ")
luvut = []

while luku!= "":
    luvut.append(luku)
    luku = input("Anna luku: ")


luvut.sort(reverse=True)
for i in range(5):
    print(luvut[i])