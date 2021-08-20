# ¿Que campeón eres del lol?

# Pregunta 1:

print("¿Que tipo de campeon del League of Legends eres?\n")

pregunta1 = "¿Eres propenso a empezar teamfigh?"

print(pregunta1 + "\n" + "-" * len(pregunta1) + "\n")

puntuacion = 0

print\
    ("(A) Si, pero muero enseguida.\n"
    "(B) Si, ademas que consigo aguantar la teamfight.\n"
    "(C) No, pero intento ayudar.\n")

sol1 = input("Respuesta: ")

# Pregunta 2:

print("\n")

pregunta2 = "Te gusta cuidar a tu equipo"

print(pregunta2 + "\n" + "-" * len(pregunta2) + "\n")

print\
    ("(A) Si, zoneo y los defiendo.\n"
    "(B) No, voy solo y solo me uno en las teamfights.\n"
    "(C) Si, intento curar o defender a mis aliados.\n")

sol2 = input("Respuesta: ")

# Pregunta 3:

print("\n")

pregunta3 = "¿Ayudas en los objetivos?"

print(pregunta3 + "\n" + "-" * len(pregunta3) + "\n")


print\
    ("(A) Si, siempre que este vivo.\n"
    "(B) Suelo ayudar la mayoría de veces, sobretodo con tp.\n"
    "(C) Solo si estoy cerca.\n")

sol3 = input("Respuesta: ")

if sol1 == "A":
    puntuacion = puntuacion + 10
elif sol1 == "B":
    puntuacion = puntuacion + 5
elif sol1 == "C":
    puntuacion = puntuacion + 0
else:
    print("Las opciones posibles son A, B y C.")
    exit()

if sol2 == "A":
    puntuacion += 5
elif sol2 == "B":
    puntuacion += 10
elif sol2 == "C":
    puntuacion += 0
else:
    print("Las opciones posibles son A, B y C.")
    exit()

if sol3 == "A":
    puntuacion += 0
elif sol3 == "B":
    puntuacion += 5
elif sol3 == "C":
    puntuacion += 10
else:
    print("Las opciones posibles son A, B y C.")
    exit()

if puntuacion > 0:
    print("Tu puntuacion es {}".format(puntuacion))

if (25 < puntuacion <= 30):
    print("Eres Asesino.")
elif (15 < puntuacion <= 25):
    print("Eres luchador.")
elif (0 < puntuacion <= 15):
    print("Eres apoyo.")

    print("Eres support.")
if puntuacion == 30:
    print("Asesino solitario.")
if puntuacion == 0:
    print("Apoyo salvavidas.")
