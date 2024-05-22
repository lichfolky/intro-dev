def max3(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    if num2 >= num1 and num2 >= num3:
        return num2
    if num3 >= num1 and num3 >= num2:
        return num3


def max_brutto(num1, num2, num3):
    return max(max(num1, num2), max(num2, num3))

def max(num1, num2):
    if num1 >= num2:
        return num1
    else:
        return num2

def max_array(array):
    massimo = 0
    for num in array:
        if massimo < num:
            massimo = num
    return massimo

print(max3(5, 46, 7))
print(max3(29, 6, 7))
print(max3(5, 9, 9))
print(max3(5, 9, 7))
print(max3(5, 6, 19))
print()
print(max_brutto(5, 46, 7))
print(max_brutto(29, 6, 7))
print(max_brutto(5, 9, 9))
print(max_brutto(5, 9, 7))
print(max_brutto(5, 6, 19))
print()
print(max_array([10,4,5,6]))