import random
import string
import hashlib
n = random.randint(0, 100)
s = ''.join(random.choices(string.ascii_lowercase, k=n))
hash_s = hashlib.sha1(s.encode('utf-8'))


def get_all_substrings(input_string):
    length = n
    return [hashlib.sha1(input_string[i:j+1].encode('utf-8')) for i in range(length) for j in range(i, length)]


count_subs = len(get_all_substrings(s))

print('Количесвто элементов =', count_subs, 'сама строка -', s, 'содержит', n, 'элементов')