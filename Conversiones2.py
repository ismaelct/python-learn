import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

# now, to clear the screen
cls()

dollar_euro = 0.85
libra_euro = 1.16

print("Conversiones: \n"
               "   ( A ) $ >> €\n"
               "   ( B ) $ >> £\n"
               "   ( C ) € >> $\n"
               "   ( D ) € >> £\n"
               "   ( E ) £ >> $\n"
               "   ( F ) £ >> €\n")
opcion = input("¿Que conversion deseas realizar?:  ")

if opcion == "A":
    dinero = float(input("Cantidad en $: "))
    conversion = (dinero * dollar_euro)
    print(str(conversion) + " €")

elif opcion == "B":
    dinero = float(input("Cantidad en $: "))
    conversion = (dinero * (dollar_euro / libra_euro))
    print(str(conversion) + " £")

elif opcion == "C":
    dinero = float(input("Cantidad en €: "))
    conversion = (dinero / dollar_euro)
    print(str(conversion) + " $")

elif opcion == "D":
    dinero = float(input("Cantidad en €: "))
    conversion = (dinero / libra_euro)
    print(str(conversion) + " £")

elif opcion == "E":
    dinero = float(input("Cantidad en £: "))
    conversion = (dinero / (dollar_euro / libra_euro))
    print(str(conversion) + " $")

elif opcion == "F":
    dinero = float(input("Cantidad en £: "))
    conversion = (dinero / libra_euro)
    print(str(conversion) + " €")