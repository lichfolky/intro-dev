# dati due array trova gli elementi in comune

array1 = ["Marco", "Emma", "Anna", "Ernesto", "Pollo"]
array2 = ["Rosso", "Giallo", "Ernesto", "Blu", "Pollo"]

## Riduco a sottoproblema:
# dato un elemento guarda se è presente nell'array2

elemento = "Ernesto"
# Ricerca lineare
for i in range(0, len(array2)):
    if array2[i] == elemento:
        print("Trovato", array2[i], "alla posizione", i)

# Ricerca lineare
for elem in array2:
    if elem == elemento:
        print("Trovato", elem)

indice = 0
for elem in array2:
    if elem == elemento:
        print("Trovato", elem, "alla posizione", indice)
    indice = indice + 1

def ricerca(elemento, array):
    for elem in array:
        if elem == elemento:
            return True
    return False

# Posso riempire man mano una lista con gli elementi che trovo
nomi_trovati = []
for elemento in array1:
    if ricerca(elemento, array2):
        nomi_trovati = nomi_trovati + [elemento]

print(nomi_trovati)