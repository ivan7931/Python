caballero = {
    "vida" : 0,
    "defensa" : 0,
    "ataque" : 2,
    "alcance" : 2,
}
guerrero = {
    "vida" : 2,
    "defensa" : 2,
    "ataque" : 0,
    "alcance" : 0
}
arquero = {
    "vida": 0,
    "defensa": 0,
    "ataque": 0,
    "alcance": 0
}
caballero["vida"] = 2 * int(guerrero.get("vida"))
caballero["defensa"] = 2 * int(guerrero.get("defensa"))
guerrero["ataque"] = 2 * int(caballero.get("ataque"))
guerrero["alcance"] = 2 * int(caballero.get("alcance"))
arquero["vida"] = guerrero.get("vida")
arquero["ataque"] = guerrero.get("ataque")
arquero["defensa"] = int(guerrero.get("defensa"))/2
arquero["alcance"] = 2 * int(guerrero.get("alcance"))
print(caballero)
print(guerrero)
print(arquero)