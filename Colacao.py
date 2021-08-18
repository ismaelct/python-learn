# Estructuras de control (if)
print("Me voy a la cocina")
print("Abro la nevera")

milk = input("¿Hay leche? (S/N)")

if milk == "S" or milk == "s":
    cocoa = input("¿Hay colacao? (S/N)")
    if cocoa == "S" or cocoa == "s":
        print(
            "Sacamos la leche de la nevera y la echamos en un vaso"
        )
        print(
              "Echamos colacao en el vaso"
        )
        print(
              "Mezclamos"
        )
    if cocoa == "n" or "N":
        print("Hay que comprar colacao")

if milk == "n" or "N":
    print("Hay que comprar leche")




print(
    "Con leche o sin leche hemos acabado"
)