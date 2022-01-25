# variables
    nombre = 'ismael'
    pi = '3.1415'

# cadenas
    solo = 'ismael'
    multi = """
                ismael
                castellanos
                talavera
            """

# numeros
    entero = 192
    decimal = 1.92

# Boelanos
    verdadero = True
    falso = False

# Tupla(tabla)
print('TUPLA')
    tabla = ("zero","one","two","three","four")
    print("0",tabla[0],"1",tabla[1],"2",tabla[2])
    #
    print("Del 1 al 4 sin incluir el 4",tabla[1:4])
    # del n hasta el final
    print("sin pasar por el cero hasta el 4",tabla[1:])
    # desde el inicio hasta n
    print("hasta el 1 primero sin incluir el primero",tabla[:1])

# Listas
print("LISTA")
    lista = ["platano","melon","manzana","pera"]
    print("primero",lista[0])
    lista.append("naranja")
    print(lista[4])

# Operadores
    # + suma
    # - resta
    # * multiplicacion
    # / division
    # ** potencia
    # // cociente de la division entera
    # % resto de la division entera

a = 1
b = 2
print("a b")
print(a,b)
a = a + b
print(a,b)
a += b
print(a,b)

    # ==
    # !=
    # >
    # <
    # >=
    # <=
    # and
        # true and true = true
        # true and false = false
    # or
        # true or true = true
        # true or false = true
        # false or false = false
    # xor
        # true xor false = true
        # true xor false = false
        # false xor false = false

# Imprimir pantalla
print("Mensaje","alerta",a,sep="_",end=" :termiando\n")

# pedir informacion
variable = input("Dime algo: ")  # raw_input()

