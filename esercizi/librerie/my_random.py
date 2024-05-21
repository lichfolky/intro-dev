import random

def shuffle(array, times):
    for i in range(0, times):
        #scambia tra loro due elementi scelti a caso 
        [indice1, indice2] = two_different_random_int(0, len(array) - 1)
        
        # Per scambiare il contenuto di due variabili
        # aux = elemento1
        # elemento1 = elemento2
        # elemento2 = aux

        aux = array[indice1]
        array[indice1] = array[indice2]
        array[indice2] = aux

        print("scambio ", indice1, indice2)


def two_different_random_int(min, max):
    if(min != max):
        num1 = random.randint(min, max)
        num2 = random.randint(min, max)
        while num1 == num2:
            num2 = random.randint(min, max)
    return [num1, num2]