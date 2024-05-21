numero_stringa = input("inserisci il tuo numero preferito: ")
numero = int(numero_stringa)

if numero == 5:
    print("che coincidenza è il mio preferito!")
else:
    print("numero inserito: " + numero_stringa)
    print("questo numero mi lascia indifferente")

# questo stampa tutti i numeri da 3 fino a 9 (10 no)
for i in range(0, 10):
     if(i >= 3):
        print(i)