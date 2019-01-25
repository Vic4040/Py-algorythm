# 2. Написать два алгоритма нахождения i-го по счёту простого числа.
# Без использования «Решета Эратосфена»;
# Используя алгоритм «Решето Эратосфена»
import cProfile


def ns(n):
    lst = []
    for i in range(2, n + 1):
        # пробегаем по списку (lst) простых чисел
        for j in lst:
            if i % j == 0:
                break
        else:
            lst.append(i)
    return lst


# python -m timeit -n 100 -s "import Eratosthenes" "Eratosthenes.ns(10)"
# 100 loops, best of 5: 5.32 usec per loop - 10
# 100 loops, best of 5: 62.3 usec per loop - 100
# 100 loops, best of 5: 1.35 msec per loop - 1000

#  1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 Eratosthenes.py:6(ns)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         4    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects} - 10

# 1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 Eratosthenes.py:6(ns)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        25    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects} - 100

# 1    0.000    0.000    0.004    0.004 <string>:1(<module>)
#         1    0.003    0.003    0.004    0.004 Eratosthenes.py:6(ns)
#         1    0.000    0.000    0.004    0.004 {built-in method builtins.exec}
#       168    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects} - 1000

def eratosthenes(n):
    sieve = list(range(n + 1))
    sieve[1] = 0
    for i in sieve:
        if i > 1:
            for j in range(i + i, len(sieve), i):
                sieve[j] = 0
    return sieve


cProfile.run('eratosthenes(1000)')

# python -m timeit -n 100 -s "import Eratosthenes" "Eratosthenes.eratosthenes(10)"
# 100 loops, best of 5: 7.88 usec per loop - 10
# 100 loops, best of 5: 45.2 usec per loop - 100
# 100 loops, best of 5: 536 usec per loop  - 1000

# 1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 Eratosthenes.py:44(eratosthenes)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         4    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects} - 10

#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 Eratosthenes.py:44(eratosthenes)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        25    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}- 100

#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 Eratosthenes.py:44(eratosthenes)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#       168    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects} - 1000
