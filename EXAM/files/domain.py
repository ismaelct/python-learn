#!/usr/bin/python3

import os

os.remove("registro_bonito.txt")

f = open("registros.txt","r")

lineas = f.readlines()

dickionario = {}

for line in lineas:
        # print("*",line.rstrip())
        table = line.split('#')
        dickionario[table[2]] = {
                "nombre": table[0],
                "pertenece": table[1],
                "correo": table[3].rstrip()
            }

for x in dickionario:
    regist = open("registro_bonito.txt", "a")
    regist.write("id {} ".format(x))
    regist.close()
    for a in dickionario[x]:
        y = dickionario[x][a]
        regist = open("registro_bonito.txt", "a")
        regist.write("{} {} ".format(a,y))
    regist.write("\n")

regist.close()
f.close()