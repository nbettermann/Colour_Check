def get_list(liste):  # Schritt 1
    return liste[0:round(len(liste) / 2)]


def count_elements(liste):
    counter = 0
    for i in range(0, len(liste)):  # Schritt 3
        if liste[i][0] == "b": counter += 1  # Schritt 2
    return counter


def check_colour(liste):
    return count_elements(get_list(liste))

# Listenformat ist: list = [[colour, number],]
