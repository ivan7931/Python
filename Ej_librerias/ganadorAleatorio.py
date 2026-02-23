import random
from traceback import print_tb


def definirGanador(*participantes):
    if not participantes:
        return "No hay participantes"
    else:
        return random.choice(participantes)

personas = input("Introduce los participantes separados por espacios").split()

ganador = definirGanador(personas)

print(ganador)
