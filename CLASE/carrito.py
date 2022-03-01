def carrito(nom, ape, *datos_clinte, **productos):
    print("Carrito de ", nom, ape)
    for p in productos:
        print(p)
    for clave in productos:
        print(productos[clave])
    return total


nombre = 'Pepe'
apellido = 'Sanchez'
prod1 = 'tomates'
prod2 = 'pepinos'
prod3 = 'pan'
prod4 = 'leche'

import = carrito(nombre,apellido,direccion,telf,prod1=2,prod2=3,prod3=3)
#        carrito = "Pepe", "Sanchez", " ", " ", "tomates" = 2, "pepinos" = 3, "pan" = 3
