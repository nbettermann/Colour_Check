def get_list(liste):  # Schritt 1
    return liste[0:round(len(liste) / 2)]


def count_elements(liste):
    counter = 0
    for i in range(0, len(liste)):  # Schritt 3
        if liste[i][0] == "b": counter += 1  # Schritt 2 + Schritt 3
    return counter


def colour_check(liste):
    tmp0 = get_list(liste)
    tmp1 = count_elements(tmp0)
    if tmp1 > len(tmp0)-tmp1: return "Es sind mehr schwarze Karten"
    else: return "Es sind mehr rote Karten"

# Listenformat ist: list = [[colour, number],]
# colour ist entweder "b" black oder "r" red
