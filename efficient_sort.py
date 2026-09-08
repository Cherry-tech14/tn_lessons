# merge sort
# A simple slice test to see how we split lists in half
'''
prices = [4.50, 3.50, 5.00, 2.00]
mid = len(prices) // 2
print(prices[:mid])
print(prices[mid:])


# A simple merge sort
def merge_sort(numbers):
    if len(numbers) <= 1:
        return numbers

    middle = len(numbers) // 2

    left = numbers[:middle]
    right = numbers[middle:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):
    result = []

    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    result.extend(left)
    result.extend(right)

    return result


numbers = [8, 3, 5, 1, 4, 2]

sorted_numbers = merge_sort(numbers)

print(sorted_numbers)


def merge(left, right):
    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result.extend(left)
    result.extend(right)
    return result
left = [2, 5, 8]
right = [1, 4, 7]

print(merge(left, right))
'''


# Quicksort__ pivot and partition
def quicksort(numbers):
    if len(numbers) <= 1:
        return numbers
    pivot = numbers[0]
    smaller = []
    larger = []
    for number in numbers[1:]:
        if number < pivot:
            smaller.append(number)
        else:
            larger.append(number)
    return quicksort(smaller) + [pivot] + quicksort(larger)

numbers = [6, 2, 8, 4, 1, 7]
print(quicksort(numbers))


# real world application
# imagine an online store has product prices:prices = [500, 120, 850, 300, 200], the website might want to show: lowest pricesfirst

numbers = [500, 120, 850, 300,200]

print(sorted(numbers))

numbers = [6, 2, 8, 4, 1, 7]
print(sorted(numbers))