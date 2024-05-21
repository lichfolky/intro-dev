def colpisci(matrice,riga,colonna):
    if riga >= len(matrice):
        return 0
    if colonna >= len(matrice[0]):
        return 0  
    return matrice[riga][colonna] > 0

def colpisci_lettere_numeri(matrice,riga_numero,colonna_lettera):
    colonna = ord(colonna_lettera) - 65
    riga = riga_numero - 1
    return matrice[riga][colonna] > 0
