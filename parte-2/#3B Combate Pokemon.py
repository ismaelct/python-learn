import random
acabar = "S"
while acabar == "S":

    # Stats Pokemon A
    pokemon_a = "Pikachu"
    vida_pokemon_a = random.randint(75,100)
    vida_actual_a = int(vida_pokemon_a)
    danno_pokemon_a = random.randint(5,15)
    ataque_rapido = int(random.uniform(0.5,1.5) * danno_pokemon_a)
    bola_voltio = int(2.5 * danno_pokemon_a)
    if vida_pokemon_a < 85:
        danno_pokemon_a += 5

    # Stats Pokemon B
    pokemon_b = "Tortoise"
    vida_pokemon_b = random.randint(75,100)
    vida_actual_b = int(vida_pokemon_b)
    danno_pokemon_b = random.randint(5,15)
    placaje = int(1.1 * danno_pokemon_b)
    hoja_afilada = 3 * danno_pokemon_b
    if vida_pokemon_b < 85:
        danno_pokemon_b += 5

    # Definicion contador de rondas
    i = 0

    # Mensaje principal
    print("Va a comenzar el combate Pokemón entre {} y {}\n".format(pokemon_a,pokemon_b))

    # Bucle de la pelea
    while vida_actual_a > 0 and vida_actual_b > 0:

        # Definicion de variables para representar la vida en %
        porcentaje_vida_a = int(((100 * vida_actual_a) / vida_pokemon_a) / 10)
        porcentaje_vida_b = int(((100 * vida_actual_b) / vida_pokemon_b) / 10)

        # Condicion para acabar con el bucle en el turno del Pokemon A o B
        if vida_actual_b <= 0 or vida_actual_a <= 0:
            break

        # Contador de rondas
        i += 1

        # Mensaje con nombres de los pokemons y sus vidas
        print("Ronda {}.\n"
              "Pikachu  [{}] {} PS\n"
              "Tortoise [{}] {} PS\n".format(i,porcentaje_vida_a * "█" + ((10 - porcentaje_vida_a) * " "),vida_actual_a
                                         ,porcentaje_vida_b * "█" + ((10 - porcentaje_vida_b) * " "),vida_actual_b))

        # Turno Pikachu
        print("Turno de {} [{}]".format(pokemon_a,porcentaje_vida_a * "█"\
                                                     + ((10 - porcentaje_vida_a) * " ")))

        # Decision de ataque poquemon 1
        ataque_cpu = random.randint(1,2)

        # Condicion de elcción de ataque y consecuencias
        if ataque_cpu == 1:
            print("{} ha usado [ataque rapido] y ha hecho {} de daño.".format(pokemon_a,ataque_rapido))
            vida_actual_b = vida_actual_b - ataque_rapido
        else:
            print("{} ha usado [bola voltio] y ha hecho {} de daño.".format(pokemon_a, bola_voltio))
            vida_actual_b -= bola_voltio
            autodanno_a = random.randint(2,5)
            vida_actual_a -= autodanno_a
            print("{} se ha hecho {} punto(s) de daño.".format(pokemon_a,autodanno_a))

        input("Presiona enter para continuar...")

        # Condicion para acabar con el bucle en el turno del Pokemon B o A
        if vida_actual_a <= 0 or vida_actual_b <= 0:
            break

        # Turno Tortoise
        print("\nTurno de {} [{}]".format(pokemon_b,porcentaje_vida_b * "█" + ((10 - porcentaje_vida_b) * " ")))

        ataque_jugador = None

        while ataque_jugador != "P" and ataque_jugador != "H":

            ataque_jugador = input("¿Cual Sera tu ataque?:\n"
                                   "[P] Placaje \\ [H] Hoja afilada\n")

        # Condicion de elcción de ataque y consecuencias
        if ataque_jugador == "P":
            print("{} ha usado [placaje] y ha hecho {} de daño.".format(pokemon_b, placaje))
            vida_actual_a -= placaje
        elif ataque_jugador == "H":
            print("{} ha usado [hoja afilada] y ha hecho {} de daño.".format(pokemon_b, hoja_afilada))
            vida_actual_a -= hoja_afilada
            autodanno_b = random.randint(1,7)
            vida_actual_b -= autodanno_b
            print("{} se ha hecho {} punto(s) de daño.".format(pokemon_b, autodanno_b))

        input("Presiona enter para continuar...\n")

    if vida_actual_a > vida_actual_b:
        print("Ha ganado {} con [{}]PS".format(pokemon_a,porcentaje_vida_a * "█" + ((10 - porcentaje_vida_a) * " ")))
    else:
        print("Ha ganado {} con [{}]PS".format(pokemon_b,porcentaje_vida_b * "█" + ((10 - porcentaje_vida_b) * " ")))
        acabar = None
        while acabar != "S" or acabar != "N":
            acabar = str(input("Quieres volver a jugar: [S]i | [N]o\n"))