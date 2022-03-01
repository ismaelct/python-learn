import random

print(open("prueba.txt", "r").read())

firmar = open("prueba.txt", "a")
firmar.write("\nFirmado por {}".format(random.randint(0,999999999999)))
firmar.close()

print(open("prueba.txt", "r").read())