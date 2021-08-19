# Estructuras de control (if)
print("Me voy a la cocina")
print("Abro la nevera")

milk = input("¿Hay leche? (S/N)")
cocoa = input("¿Hay colacao? (S/N)")

if milk != "S" or cocoa != "S":
    print("Voy a comprar al super...")
    if milk != "S":
        print("Compro leche")
    if cocoa != "S":
        print("Compro colacao")

if milk == "S":
    print("Sacamos la leche de la nevera y la echamos en un vaso")
if cocoa == "S" and milk == "S":
    print("Echamos el colacao")
print("Con leche o sin leche hemos acabado")
print("Mezclamos")