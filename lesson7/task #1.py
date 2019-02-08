import random

SIZE = 30
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
array2 = array
array3 = array
print(array)

n = 1
while n < len(array):
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            array[i], array[i + 1] = array[i + 1], array[i]
    n += 1
print(array)


def sort(x):
    f = 1
    while f < len(x):
        for i in range(len(x) - 1):
            if x[i] > x[i + 1]:
                x[i], x[i + 1] = x[i + 1], x[i]
        f += 1
    return x


print(sort(array2))


def sort2(y):
    left = 0
    right = len(y) - 1

    while left <= right:
        for i in range(left, right, +1):
            if y[i] > y[i + 1]:
                y[i], y[i + 1] = y[i + 1], y[i]
        right -= 1

        for i in range(right, left, -1):
            if y[i - 1] > y[i]:
                y[i], y[i - 1] = y[i - 1], y[i]
        left += 1

    return y


print(sort2(array3))
