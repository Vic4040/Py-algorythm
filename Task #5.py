# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
import random

SIZE = 5
MIN_ITEM = -100
MAX_ITEM = 99
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

i = 0
pos = -1
while i < SIZE:
    if array[i] < 0 and pos == -1:
        index = i
    elif array[pos] < array[i] < 0:
        index = i
    i += 1

print(pos + 1, ':', array[pos])
