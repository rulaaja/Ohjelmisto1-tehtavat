
vuodenpäivät = ("talvi","talvi",
                "kevät", "kevät", "kevät" ,
                "kesä" , "kesä", "kesä",
                "syksy", "syksy", "syksy",
                "talvi")
järjestysnumero=int(input("Anna kuukauden numero (1-12): "))
vuodenpäivä = vuodenpäivät[järjestysnumero-1]
print (f"{järjestysnumero}. viikonpäivä on {vuodenpäivä}.")