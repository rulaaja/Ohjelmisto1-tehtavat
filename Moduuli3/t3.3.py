sukupuoli=input("Oletko Mies vai Nainen? " )
hemo=float(input("Mikä on hemoglobiiniarvosi? "))

if sukupuoli=="Mies" and hemo>194:
    print("Arvosi ovat liian korkeat")
elif sukupuoli=="Mies" and hemo>134 and hemo<194:
    print("Arvosi ovat normaalit")
elif sukupuoli=="Mies" and hemo<134:
    print("Arvosi ovat liian alhaiset")

if sukupuoli=="Nainen" and hemo>175:
    print("Arvosi ovat liian korkeat")
elif sukupuoli=="Nainen" and hemo>117 and hemo<175:
    print("Arvosi ovat normaalit")
elif sukupuoli=="Nainen" and hemo<117:
    print("Arvosi ovat liian alhaiset")



