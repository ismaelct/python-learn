#!/usr/bin/env python3class Persona:
    def __init__(self, nombre, edad, altura, peso):
        self.nom = nombre
        self.edad = edad
        self.h = altura
        self.p = peso
import os
if os.name == "posix":
    os.system("clear")
    print("unix")
elif os.name == "nt":
    os.system("cls")
    print("windows")
