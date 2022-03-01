import random

numero_ganador = random.randint(1, 10)

print("Tienes que adivinar un numero del 1 al 10.")

numero_elegido = int(input("¿Cual crees que es el número?: "))

if numero_elegido == numero_ganador:
    print("Enhorabuena has acertado")

print("El numero ganador erá: {}".format(numero_ganador))
print("Fin del juego.")