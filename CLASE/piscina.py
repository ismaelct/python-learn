import os

if os.name == "posix":
    os.system("clear")
elif os.name == "nt":
    os.system("cls")

# alumnos = {'%dni%':{'nombre':'%nombre%','apellidos':'%apellido%','edad':0,'curso':"%curso%",'notas':[]}}
alumnos = {}


op = int(input('''
    1. Añadir usurios
    2. Borrar usuarios
    3. Consultar usuarios
    4. Listar usuarios
    5. Salir
    > '''))

if op == 1:
    print("añadir")
    dni = input("DNI: ")
    nombre = input("NOMBRE: ")
    apellidos = input("APELLIDOS: ")
    edad = int(input("EDAD: "))
    curso = input("CURSO: ")
    nota1 = input("NOTAS 1: ")
    nota2 = input("NOTAS 2: ")
    nota3 = input("NOTAS 3: ")

    alumnos.update({dni:{}})
    alumnos[dni]['nombre'] = nombre.upper()
    alumnos[dni]['apellido'] = apellidos.upper()
    alumnos[dni]['edad'] = edad
    alumnos[dni]['curso'] = curso

    # LISTA TEMPORAL
    notas.append(nota1)
    notas.append(nota2)
    notas.apped(nota3)
    alumnos[dni]['notas'] = notas
    print(alumnos[dni]["notas"])
elif op == 2:
    print("borrar")
elif op == 3:
    print("consultar")
else:
    exit