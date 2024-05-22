def istogramma(data):
    for dato in data:
        print("*" * dato)


istogramma([3, 4, 5, 5, 2])

""" 
0: ***
1: ****
2: *****
3: *****
4: ** 
"""

def istogramma_numeri(data):
    for i in range(len(data)):
        print(str(i) + ": ", "*" * data[i], sep="")

print()
istogramma_numeri([3, 4, 5, 5, 2])
