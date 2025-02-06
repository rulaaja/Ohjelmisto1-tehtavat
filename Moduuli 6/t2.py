import math
import random

satunnainen=random.randint(1,6)
tahko=int(input("Tahkojen määrä: "))

def laske(x):
    while True:
        satunnainen = random.randint(1, tahko)
        print(f"Heitetään noppaa uudestaan: Luku on {satunnainen}")
        if satunnainen==tahko:
            print("Maksimiluku!")
            break

laske(satunnainen)