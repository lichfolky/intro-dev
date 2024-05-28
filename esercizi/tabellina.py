'''
numero = int(input("dai metti un numero"))

for molt in range(1, 11):
    print(molt * numero, end=" ")
'''
for numero in range(1, 11):
    for molt in range(1, 11):
        print(molt * numero, end=" ")
    print()

