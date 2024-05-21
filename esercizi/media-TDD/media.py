
## array = [3, 4, 5, 6, 7, 43, 21, 2, 3, 4]
# 9.8

# trovo la media di un array
def media(array):
    # conto elementi array
    numero_elementi = len(array)
    # sommo elementi array
    somma = 0
    for elemento in array:
        somma = somma + elemento  # accumulatore
    # divido somma per numero_elementi
    if numero_elementi > 0:
        media = somma / numero_elementi
        return media
    else:
        return 0
