import math

leiviska = float(input("Anna leiviskät "))
naulat = float(input("Anna naulat "))
luodit = float(input("Anna luodit "))
leiviskatulos = int(leiviska*20*32*13.3)
naulatulos= int(naulat*32*13.3)
luotitulos=int(luodit*13.3)
tulos_grammoissa=naulatulos+leiviskatulos+luotitulos
tulos_kiloissa=float(tulos_grammoissa/1000)
tulos_grammoissa=float(tulos_kiloissa*1000)
print(f"Massa nykymittojen mukaan: {tulos_kiloissa} KILOGRAMMAA {tulos_grammoissa} GRAMMAA")
