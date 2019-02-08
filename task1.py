# try:
#    n = int(input('please enter fibonacci array member N here: '))
# except ValueError:
#
#    print("input numbers only")
#    exit(1)

# python -m timeit -n 100 -s "import task1" "task1.fib(10)"


import cProfile


def fib(n):     # return Fibonacci series up to n
    """ряд фибоначчи по N"""
    result = []
    a, b = 1, 1
    while b < n ** 100:
        result.append(b)
        a, b = b, a + b
    return result


# сложность 10
# 100 loops, best of 5: 2.64 usec per loop
# сложность 100
# 100 loops, best of 5: 7.45 usec per loop
# слоэность 1000
# 100 loops, best of 5: 9.35 usec per loop
# увеличили петли до 1000
# 1000 loops, best of 5: 8.84 usec per loop

# cProfile.run('fib(1000)')

# 1    0.000    0.000    0.002    0.002 <string>:1(<module>) - 10
#         1    0.002    0.002    0.002    0.002 task1.py:14(fib)
#         1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
#       957    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# 1    0.000    0.000    0.003    0.003 <string>:1(<module>)
#         1    0.003    0.003    0.003    0.003 task1.py:14(fib)
#         1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
#       957    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# 1       0.001    0.001    0.007    0.007 <string>:1(<module>)
#         1    0.006    0.006    0.006    0.006 task1.py:14(fib)
#         1    0.000    0.000    0.007    0.007 {built-in method builtins.exec}
#      1436    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

def fib_test(n):
    fib_d = {0: 0, 1: 1}

    def _fib_test(n):
        if n in fib_d:
            return fib_d[n]
        fib_d[n] = _fib_test(n - 1) + _fib_test(n - 2)
        return fib_d[n]

    return _fib_test(n)


# 100 loops, best of 5: 6 usec per loop    - 10
# 100 loops, best of 5: 62.8 usec per loop - 100
# 100 loops, best of 5: 176 usec per loop  - 250
# 100 loops, best of 5: 384 usec per loop  - 500

cProfile.run('fib_test(500)')

#         1    0.000    0.000    0.000    0.000 <string>:1(<module>) - 10
#         1    0.000    0.000    0.000    0.000 task1.py:54(fib_test)
#      19/1    0.000    0.000    0.000    0.000 task1.py:57(_fib_test)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

#  1    0.000    0.000    0.000    0.000 <string>:1(<module>) - 100
#         1    0.000    0.000    0.000    0.000 task1.py:54(fib_test)
#     199/1    0.000    0.000    0.000    0.000 task1.py:57(_fib_test)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# 1    0.000    0.000    0.001    0.001 <string>:1(<module>) - 250
#         1    0.000    0.000    0.001    0.001 task1.py:54(fib_test)
#     499/1    0.001    0.000    0.001    0.001 task1.py:57(_fib_test)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# 1    0.000    0.000    0.001    0.001 <string>:1(<module>) - 500
#         1    0.000    0.000    0.001    0.001 task1.py:54(fib_test)
#     999/1    0.001    0.000    0.001    0.001 task1.py:57(_fib_test)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}