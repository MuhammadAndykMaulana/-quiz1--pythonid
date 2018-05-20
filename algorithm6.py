#!/usr/bin/python3
from itertools import accumulate, filterfalse

a = 9
b = (4, 2, 1, 5, 6, 3)
print('stop pada urutan ke {}'.format((len(list(filterfalse(lambda x: x > a, accumulate(b)))) + 1)))
