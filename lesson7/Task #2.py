import random

SIZE = 30
MIN_ITEM = 0
MAX_ITEM = 49
sample = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]


def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2
        lefthalf = array[:mid]
        righthalf = array[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                array[k] = lefthalf[i]
                i = i + 1
            else:
                array[k] = righthalf[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            array[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            array[k] = righthalf[j]
            j = j + 1
            k = k + 1
    return array


print(merge_sort(sample))

