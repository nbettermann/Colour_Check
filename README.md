# **Vergleich der Anzahl der roten und schwarzen Karten (Funkion: colour_check)**
## Funktion:
###  - Es soll ermittelt werden, ob sich in der ersten Hälfte des Kartendecks mehr rote als schwarze Karten befinden.

## Anforderungen:
### - Es befinden sich im Kartendeck 32 Karten.
### - Eine Karte kann entweder rot oder schwarz sein.

### Visualisierung:
![](Visualisierung.png)

## Teilprobleme:
### 1. Ausgabe der ersten Hälfte des Kartendecks (Funktion: get_list)
### 2. Prüfen, ob es sich um eine rote Karte handelt (Funktion: count_elements)
### 3. Schritt 2. mit allen Karten durchführen und die Schwarzen Zählen (Funktion: count_elements)
### 4. die schwarzen mit den roten Karten vergleichen (Funktion: count_elements)
![](Teil_Probleme.png)

## Input:
### - Akzeptierter Input für die Funktion: array = [[colour, number], …]
### - colour ist entweder "b" black oder "r" red
