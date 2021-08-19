numero_ganador = 3

print("Tienes que adivinar un numero del 1 al 10.")

numero_elegido = int(input("¿Cual crees que es el número?: "))


if numero_elegido == numero_ganador:
    print("Enhorabuena has acertado")

print("Fin del juego.")