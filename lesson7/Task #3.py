import random
from statistics import median

m = random.randint(0, 10)
SIZE = 2 ** (m + 1)
MIN_ITEM = 0
MAX_ITEM = 1000
sample = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(SIZE)

def med(l, pivot_fn=random.choice):

    if len(l) % 2 == 1:
        return quickselect(l, len(l) / 2, pivot_fn)
    else:
        return 0.5 * (quickselect(l, len(l) / 2 - 1, pivot_fn) +
                      quickselect(l, len(l) / 2, pivot_fn))


def quickselect(l, k, pivot_fn):

    if len(l) == 1:
        assert k == 0
        return l[0]

    pivot = pivot_fn(l)

    lows = [el for el in l if el < pivot]
    highs = [el for el in l if el > pivot]
    pivots = [el for el in l if el == pivot]

    if k < len(lows):
        return quickselect(lows, k, pivot_fn)
    elif k < len(lows) + len(pivots):

        return pivots[0]
    else:
        return quickselect(highs, k - len(lows) - len(pivots), pivot_fn)


print(med(sample, random.choice))
print(median(sample))
