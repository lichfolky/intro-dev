# dati due array trova gli elementi in comune

array1 = ["Marco", "Emma", "Anna", "Ernesto"]
array2 = ["Rosso", "Giallo", "Ernesto", "Blu"]

## Riduco a sottoproblema:
# dato un elemento guarda se è presente nell'array2

elemento = "Ernesto"
# Ricerca lineare
for i in range(0, len(array2)):
    if array2[i] == elemento:
        print("Trovato",array2[i],"alla posizione", i)

# Ricerca lineare
for elem in array2:
    if elem == elemento:
        print("Trovato",elem)