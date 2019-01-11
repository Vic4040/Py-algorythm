# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами минимальный
# и максимальный элементы в сумму не включать.

import random

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 99
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
ttl = 0
print(array)

xs = 0
xl = 0
for i in range(SIZE):
    if array[i] < array[xs]:
        xs = i
    elif array[i] > array[xl]:
        xl = i
for i in range(xs + 1, xl):
    ttl += array[i]
print(ttl)
