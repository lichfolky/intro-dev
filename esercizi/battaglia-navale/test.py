import battaglia_navale

matrice1 = [[1, 0, 0, 2, 2], 
           [1, 0, 0, 0, 3], 
           [1, 0, 1, 0, 3], 
           [1, 0, 1, 0, 3]]

matrice2 = [
    [True, False, False, True, True],
    [True, False, False, False, True],
    [True, False, True, False, True],
    [True, False, True, False, True],
]

matrice3 = [
    [1, 0, 0, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
]

# Test 0: verifica la tua conoscenza della matrici:
if matrice2[2][1] == False:
    print("test 0: superato!")
else:
    print("test 0: fallito!")

risultato = battaglia_navale.colpisci(matrice1, 3, 3)

if risultato == False:
    print("test 1: superato!")
else:
    print("test 1: fallito!")

if battaglia_navale.colpisci(matrice1, 0, 0) == True:
    print("test 2: superato!")
else:
    print("test 2: fallito!")

if battaglia_navale.colpisci(matrice1, 99, 99) == False:
    print("test 3: superato!")
else:
    print("test 3: fallito!")

if battaglia_navale.colpisci_lettere_numeri(matrice1, 1, 'A') == True:
    print("test 4: superato!")
else:
    print("test 4: fallito!")
