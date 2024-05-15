import random
import moduli.my_random as my_random

numeri = [3, 2, 5, 6]
animali = ["leone", "panda", "gatto", "merlo", "tigre"]

matrice = [[1,2,3],
           [4,5,6],
           [7,8,9]]

def print_matrix(matrix):
    for row in matrix:
        for element in row:
            print(element, " ", end='')
        print()

print_matrix(matrice)


bicchieri = [True, False, False]
print(bicchieri)
my_random.shuffle(bicchieri, 5)

## qui chiamo la funzione shuffle della libreria random
# print(random.shuffle(bicchieri))
print(bicchieri)

bicchiere_scelto = int(input("scegli un bicchiere ")) - 1
print(bicchieri[bicchiere_scelto])