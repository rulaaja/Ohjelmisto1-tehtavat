import math

luku=int(input("Anna luku: "))
luvut = []

if luku <2:
    print("Luku ei ole alkuluku")

elif luku % 1 != 0:
    print("Luku ei ole alkuluku")

else:
    for i in range(2, luku):
        if luku % 1 == 0:
            print(f"Luku on alkuluku")