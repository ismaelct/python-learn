import os

if os.name == "posix":
    os.system("clear")
elif os.name == "nt":
    os.system("cls")

#   variables
nombre = 'ismael'  # strings
pi = '3.1415'  # numeros

#   cadenas
solo = 'ismael'  # one-line
multi = """
ismael
castellanos
talavera
"""  # multi-line

#   numeros
entero = 192  # entero
decimal = 1.92  # decimal

#   Boelanos
verdadero = True  # Verdadero
falso = False  # Falso


#   Tupla(tabla)
print('TUPLA')
tupla = ("zero", "one", "two", "three", "four")
print("0", tupla[0], "1", tupla[1], "2", tupla[2])
#
print(tupla[1:4])
# del n hasta el final
print(tupla[1:])
# desde el inicio hasta n
print(tupla[:1])

# Listas
print("LISTA")
lista = ["platano", "melon", "manzana", "pera"]

# insertar en lista
print("primero", lista[0])
lista.append("naranja")
print(lista[4])
lista = lista + ["melocotón"]
print(lista[5])
print(lista)
lista.insert(4, "piña")
print(lista)

# borrar de la lista
print("Quitar el platano", lista)
lista.remove("platano")
print("Quitar el platano", lista)
print("Quitar el n=0", lista)
lista.pop(0)
print("Quitar el n=0", lista)
print("Quitar el ultimo", lista)
lista.pop()
print("Quitar el ultimo", lista)

# ordenar lista

# a-z (de forma permanente)
lista.sort()
# z-a
lista.sort(reverse=True)

# contar un elemento en una lista
lista.count("platano")

# Listas e indices
print("La lista es", lista, "y 'piña' esta el nº", lista.index("piña"))

# Funciones para listas y tuplas
tupla1 = (1, 2, 3, 4)
lista1 = ["uno", "dos", "tres", "cuatro"]

# transformar una tupla en lista (de manera no permanente es solo co la funcion)
list(tupla1)
# trasformar tupla a lista
tuple(lista1)
# func
max(lista1)  # tupla1) # elemento max
min(lista1)  # tupla1) # elemento min
len(lista1)  # tupla1) # nº elementos
# concatenar lista y tupla
listax = lista1 + lista2
tuplax = tupla1 + tupla2
# copiar
# (enlace)linkeado
lista1 = lista2
# sin linkear
lista1 = lista2[:]

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
print(a, b)
a = a + b
print(a, b)
a += b
print(a, b)

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
print("Mensaje", "alerta", a, sep="_", end=" :termiando\n")

# pedir informacion
# variable = input("Dime algo: ")  # raw_input()

# diccionarios
diccionario = {'Espanna': 'Madrid', 'Italia': 'Roma'}
diccionario['Espanna']  # madrid
diccionario.items
diccionario.keys
diccionario.values
diccionario.clear