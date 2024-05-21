# Return double of n
def addition(n):
    return n + n


numbers = [1, 2, 3, 4]

result = []
for number in numbers:
    result.append(addition(number))
print(result)

# We double all numbers using map()
result = map(addition, numbers)
print(list(result))
