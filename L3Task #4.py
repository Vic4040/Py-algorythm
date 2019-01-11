# Определить, какое число в массиве встречается чаще всего.
import random

SIZE = 500
MIN_ITEM = 1
MAX_ITEM = 99
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

x = array[0]
max_count = 1
for i in range(SIZE - 1):
    count = 1
    for n in range(i + 1, SIZE):
        if array[i] == array[n]:
            count += 1
    if count > max_count:
        max_count = count
        x = array[i]

if max_count == 1:
    print('совпадений не случилось - все элементы неповторимы')
else:
    print(x, 'встречается', max_count, 'раз')
