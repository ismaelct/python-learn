# Escapa de pandora
victoria = ("""
██╗   ██╗██╗ ██████╗████████╗ ██████╗ ██████╗ ██╗ █████╗     
██║   ██║██║██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗██║██╔══██╗    
██║   ██║██║██║        ██║   ██║   ██║██████╔╝██║███████║    
╚██╗ ██╔╝██║██║        ██║   ██║   ██║██╔══██╗██║██╔══██║    
 ╚████╔╝ ██║╚██████╗   ██║   ╚██████╔╝██║  ██║██║██║  ██║    
  ╚═══╝  ╚═╝ ╚═════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝    
                                                             
""")

derrota = ("""
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
      "Lo último que recuerdas, a dos robots humanoides que te llevaron a la fuerza.\n\n"
      "Tienes dos opciones apartir de aqui:\n"
      "( A ) Tratar de forzar la sala para salir.\n"
      "( B ) Utilizar el destornillador multiuniversal del profesor.\n")

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
                  "llevarlos a la Tierra. Y acabaís en la Tierra sanos y a salvo.")
            print(victoria)
      else:
            print("Tratas de correr hacia la nave, en el proceso los guardias te persiguen.\n"
                  "Cuando llegas a la nave te das cuenta que no sabes como pilotarla y empiezas\n"
                  "a tocar todo. Derrepente empieza a brillar todo en rojo y aparece lo que parece\n"
                  "una cuenta atrás. Cuando acaba la nave explota contigo dentro.\n")
            print(derrota)
else:
