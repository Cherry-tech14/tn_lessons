# swapping elements
'''
numbers = [10, 20]
numbers[0], numbers[1] = numbers[1], numbers[0]
print(numbers)

numbers = [5, 2, 8]

numbers[0], numbers[1] = numbers[1], numbers[0]

print(numbers)


# bubble sort(adjacent swaps)
numbers = [5, 2, 8, 1, 3]
for i in range(len(numbers)):
    for j in range(len(numbers) - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j+1] = numbers[j +1], numbers[j]
print(numbers)
'''

# selection sort
numbers = [5, 2, 8, 1, 3]

for i in range(len(numbers)):
    smallest = i

    for j in range(i + 1, len(numbers)):
        if numbers[j] < numbers[smallest]:
            smallest = j

    numbers[i], numbers[smallest] = numbers[smallest], numbers[i]

print(numbers)

# insertion sort
numbers = [5, 2, 8, 1, 3]

for i in range(1, len(numbers)):
    current = numbers[i]
    j = i - 1

    while j >= 0 and numbers[j] > current:
        numbers[j + 1] = numbers[j]
        j = j - 1

    numbers[j + 1] = current

print(numbers)