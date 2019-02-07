import math
# multiply two integers using karatsuba multiplication
import time


def karatsuba(a, b):

    # print type(a), type(b), a, b
    if int(a) < 10 or int(b) < 10:
        return int(a) * int(b)

    # find optimal place to separate digits
    maxlen = min(len(a), len(b))
    maxlen = maxlen - 1 if maxlen % 2 != 0 else maxlen
    maxlenby2 = maxlen / 2

    # separate digits
    highnum_a, lownum_a = int(a[:-maxlenby2]), int(a[-maxlenby2:])
    highnum_b, lownum_b = int(
        b[:-maxlenby2]), int(b[-maxlenby2:])

    # perform recursion
    z2 = karatsuba(str(highnum_a), str(highnum_b))
    z1 = karatsuba(str(highnum_a + lownum_a), str(highnum_b + lownum_b))
    z0 = karatsuba(str(lownum_a), str(lownum_b))
    result = z2 * (10**maxlen) + (z1 - z2 - z0) * (10**maxlenby2) + z0
    # print highnum_a, lownum_a, highnum_b, lownum_b, z2 * (10**maxlen), (z1 - z2 - z0) * (10**maxlenby2), z0, result, maxlen, maxlenby2
    return result


with open('numbers.txt') as fp:
    lines = [tuple(f.strip().split(", ")) for f in fp.readlines()]

for everytest in lines:
    a = everytest[0]
    b = everytest[1]
    # t = time.time()
    print a, b, karatsuba(a, b) == (int(a)*int(b)) 
    # print time.time(), t
