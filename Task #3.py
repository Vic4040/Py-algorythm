# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random

SIZE = 10
MIN_ITEM = 1
MAX_ITEM = 99
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

xs = 0
xl = 0
for i in range(SIZE):
    if array[i] < array[xs]:
        xs = i
    elif array[i] > array[xl]:
        xl = i
print('исходный вид массива', array)
print('array[%d]=%d array[%d]=%d' % (xs + 1, array[xs], xl + 1, array[xl]))
z = array[xs]
array[xs] = array[xl]
array[xl] = z
print(array)
