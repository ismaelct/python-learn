a = int(
    input(
        "Dime un número: "
    )
)
b = int(
    input(
        "Dime otro número: "
    )
)
c = int(
    input(
        "Dime un último número: "
    )
)
# print("el mínimo es:", min(a, b, c))
# print("el máximo es:", max(a, b, c))
print("el número mínimo entre {}, {}, {} es {} y el número máximo es {}".format(a, b, c, min(a, b, c),
                                                                                               max(a, b, c)))
