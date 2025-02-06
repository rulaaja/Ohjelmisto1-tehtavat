import math
import random

satunnainen=random.randint(1,6)

def laske(x):
    while True:
        satunnainen = random.randint(1, 6)
        print(f"Heitetään noppaa uudestaan: Luku on {satunnainen}")
        if satunnainen==6:
            print("Luku on 6")
            break

laske(satunnainen)
