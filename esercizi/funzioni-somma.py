numeri = [56, 43 , 22, 4, 77, 23, 33]
somma = sum(numeri)

# definizione della funzione 
def mia_somma(a, b):
    risultato = a + b
    return risultato

# chiamata funzione
print("la mia somma: " + str(mia_somma(2,54)))

def somma_array(array):
    somma = 0
    for i in range(0,len(array)):
       somma = somma + array[i]
    return somma

def somma_array_easy(array):
    somma = 0
    for elemento in array:
       somma = somma + elemento
    return somma

print(somma_array_easy([2,3,4,6,3,56,7,3]))