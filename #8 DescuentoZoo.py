edad = int(input("¿Que edad tienes?: "))
tipo_carnet = input("¿Cuentas con algun carnet? (E Estudiante / J Jubilado / F Familia Numerosa / N Ningúno): ")

if (25 <= edad <= 35 and tipo_carnet == "E") or \
        edad <= 10 or \
        (edad <= 65 and tipo_carnet == "J") or \
        tipo_carnet == "F":
    print("Eres candidato para el descuento.")
else:
    print("No eres candidato del descuento")