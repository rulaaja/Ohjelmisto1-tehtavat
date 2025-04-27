class Hissi:
    def __init__(self, alin, ylin):
        self.alin=alin
        self.ylin=ylin
        self.nykyinen_kerros = alin


    def ylos(self):
        self.nykyinen_kerros +=1
        print(f"hissi menee ylös, olen kerroksessa {self.nykyinen_kerros}")


    def alas(self):
        self.nykyinen_kerros -= 1
        print(f"hissi menee alas, olen kerroksessa {self.nykyinen_kerros}")

    def siirry_kerrokseen(self, tavoitekerros):
        while tavoitekerros > self.nykyinen_kerros and 8>tavoitekerros>1:
            self.ylos()

        while tavoitekerros < self.nykyinen_kerros and 8>tavoitekerros>1:
            self.alas()

        print(f"olen kerroksessa {self.nykyinen_kerros}")
        pass

class Talo:
    def __init__(self, hissit, alin, ylin):
        self.alin = alin
        self.alin = ylin
        self.hissit = []
        for i in range(hissit):
            self.hissit.append(hissit)

    def ajahissia(self, hissit, tavoitekerros):
        if tavoitekerros > self.nykyinen_kerros and 8 > tavoitekerros > 1:
            self.ylos()
        if tavoitekerros < self.nykyinen_kerros and 8 > tavoitekerros > 1:
            self.alas()
        hissit[1]



testiHissi= Hissi(1, 7)
testiTalo= Talo(2, 1, 7)

print(f"hissi on {testiHissi.nykyinen_kerros} kerroksessa")

testiHissi.siirry_kerrokseen(2)
