
litra=float(3.785)

def lasku():
    while True:
        gal=float(input("Anna galloonat: "))
        if gal <= 0:
            break
        if gal>=0:
            print(f"Litroina: {gal*litra}")


lasku()
