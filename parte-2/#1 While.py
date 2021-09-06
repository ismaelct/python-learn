respuesta = None

while respuesta != 'A' and respuesta != 'B' and respuesta != 'C':
    respuesta = input('¿Opción [A, B, C]?')

    if respuesta == "A":
        print("Has elegido bien\n")

    elif respuesta == "B":
        print("Podrias haber elegido mejor\n")

    elif respuesta == "C":
        print("Podrias haber elegido peor\n")

    else:
        print("Respuesta sin sentido\n")