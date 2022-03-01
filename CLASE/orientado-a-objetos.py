import os
import datetime


# POO es otro paradigma de progrmación
#
#
# todo sera un objeto y los objetos tienen atributos y se utilizan con metodos

# Las clases: son modelos sobre los que se constryen los objetos

# La clase "MyClass" con la propiedad x, que vale 5
class MyClass:
    x = 5


# El objeto obj1
obj1 = MyClass()
print(obj1.x)


class Persona:
    def __init__(self, nombre, edad, altura, peso):
        self.nom = nombre
        self.edad = edad
        self.h = altura
        self.p = peso

    def calculaedad(self):
        year = 2022
        return year - self.edad

    def prestar(self):
        print("Hola soy,",self.nom+". Tengo",self.edad,"años y mis caracteristicas son:\n\tAltura", self.h ,"CM \n\tPeso", self.p, "KG")


p1 = Persona("Alberto", 50,"","")

print(p1.nom, "Tiene", p1.edad,"\n")

p2 = Persona("Juan", 40,"","")

print(p2.nom, "Tiene", p2.edad)
print("año nacimiento", p2.calculaedad(),"\n")

p3 = Persona("Ismael", 21, 1.85, 80)

p3.prestar()

class Alumno(Persona):
    def __init__(self,nota,nom,edad,h,p):
        Perosna.__init__(self,nom,edad,h,p)
        self.nota = nota
    def metodo(self):
        print(self.nota,self.nom,self.edad,self.h,self.p


