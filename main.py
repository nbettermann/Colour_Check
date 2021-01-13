def get_list(liste):
    return liste[0:round(len(liste) / 2)]


def count_elements(liste):
    counter = 0
    for i in range(0, len(liste)):
        if liste[i][0] == "b": counter += 1
    return counter


def check_colour(liste):
    return count_elements(get_list(liste))

# Listenformat ist: list = [[colour, number],]
