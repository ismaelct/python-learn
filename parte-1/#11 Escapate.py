# Escapa de pandora
import random
victoria = ("""
██╗   ██╗██╗ ██████╗████████╗ ██████╗ ██████╗ ██╗ █████╗     
██║   ██║██║██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗██║██╔══██╗    
██║   ██║██║██║        ██║   ██║   ██║██████╔╝██║███████║    
╚██╗ ██╔╝██║██║        ██║   ██║   ██║██╔══██╗██║██╔══██║    
 ╚████╔╝ ██║╚██████╗   ██║   ╚██████╔╝██║  ██║██║██║  ██║    
  ╚═══╝  ╚═╝ ╚═════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝    
                                                             
""")

derrota = ("""/home/angar/repos/python-learn/venv/bin/python "/home/angar/repos/python-learn/parte-1/#1 PrimeraPrueba.py"
¿Como te llamas? ismael
Tu nombre es ismael
4

Process finished with exit code 0

██████╗ ███████╗██████╗ ██████╗  ██████╗ ████████╗ █████╗ 
██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔═══██╗╚══██╔══╝██╔══██╗
██║  ██║█████╗  ██████╔╝██████╔╝██║   ██║   ██║   ███████║
██║  ██║██╔══╝  ██╔══██╗██╔══██╗██║   ██║   ██║   ██╔══██║
██████╔╝███████╗██║  ██║██║  ██║╚██████╔╝   ██║   ██║  ██║
╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚═╝  ╚═╝
                                                          
""")

print("Te despiertas y estas en un asiento, en un lugar oscuro.\n"
      "Se encienden las luces y ves que estas en una sala pequeña,\n"
      "en la que estas solo tú. \n"
      "Lo último que recuerdas, a dos robots humanoides que te llevaron a la fuerza.\n"
      "Te das cuenta que tienes el destornillador de tu amigo el Doctor Who \n"
      "y que podrías pedirle ayuda.\n\n"
      "Tienes dos opciones apartir de aqui:\n"
      "( A ) Tratar de forzar la sala para salir.\n"
      "( B ) Utilizar el destornillador sonico del doctor who.\n")

A = input("Tú decisión: ")

if A == "A" or A == "a":
      print("\nTras horas intentandolo, consigues salir de la caja de pandora.\n"
            "Aun que estas exhausto, sigues y admiras el lugar donde estas,\n"
            "estas en un planeta que no parece la Tierra. Decides moverte,\n"
            "pero ves los mismos robots que te capturaron, estan haciendo guardia.\n"
            "Mientras te mueves ves dos cosas, a lo lejos ves lo que parecen unas naves \n"
            "y mas adelante ves mas cubiculos como del que saliste tú,\n"
            "donde parece haber mas humanos.\n\n"
            "Tienes que tomar una decisión:\n"
            "( A ) Decides ir a investigar los cubiculos.\n"
            "( B ) Prefieres robar una de las naves y volver a la Tierra.\n")
      A = input("Tú decisión: ")

      if A == "A" or A == "a":
            print("Consigues liberar a 1 persona y otra forma de vida,\n"
                  "lo que denominarias como reptiliano. Los dos juntos con el reptiliano\n"
                  "os poneis de acuerdo para robar la nave, el repitiliano promete\n"
                  "llevarlos a la Tierra. Y acabaís en la Tierra sanos y a salvo.\n"
                  + victoria)

      else:
            print("Tratas de correr hacia la nave, en el proceso los guardias te persiguen.\n"
                  "Cuando llegas a la nave te das cuenta que no sabes como pilotarla y empiezas\n"
                  "a tocar todo. Derrepente empieza a brillar todo en rojo y aparece lo que parece\n"
                  "una cuenta atrás. Cuando acaba la nave explota contigo dentro.\n"
                  + derrota)

else:
      print("Decides utilizar el destorillador que tienes del profesor y te deja llamar al doctor.\n\n"
            "Tienes que tomar una decisión:\n"
            "( A ) Llamas al doctor y le pides ayuda.\n"
            "( B ) No llamas al doctor.\n")
      A = input("Tú decisión: ")

      if A == "A" or A == "a":
            llamada_doctor = 1

      else:
            llamada_doctor = 0
      numeroa = random.randint(1, 10)
      numerob = random.randint(1, 10)
      print("\nTe encuentras con los robots humanoides, pero te proponen dejarte libre,\n" +
            "deberás resolver la siguiente operación: ({} * {})\n".format(numeroa,numerob) +
            "De lo contrario te devolverán a la caja de Pandora.\n"
            "( A ) Decides resolver la formula.\n"
            "( B ) Te rebelas ante los robots.\n")
      f = numeroa * numerob
      A = input("Tu decisión: ")

      if A == "A" or A == "a":
            A = input("¿Cuál es la solución?: ")

            if int(A) == int(f):
                  print("\n¡Tus calaculos son correctos!\n"
                        "Te liberan y te llevan de vuelta a la Tierra.\n"
                        + victoria)

            else:
                  print("\nNoo, suspendiste matematicas. Al pozo, mejor dicho a la Pandorica."
                        + derrota)

      else:

            if llamada_doctor == 1:
                  print("\nDecidiste no resolverlo y te van a llevar a la Pandorica.\n"
                  "Pero derrepente.. *Sonidos de tardis*\n"
                  "El doctor aparece con la tardis, acudiendo a tu llamada de socorro.\n"
                  "Estas salvado.\n" + victoria)

            else:
                  print("\nDecidiste no resolverlo y te van a llevar a la Pandorica.\n"
                        "Ya no hay vuelta atrás, seras encerrado en la Pandorica..\n"
                        + derrota)
