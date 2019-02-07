
def fastpower(a, b):

    print a, b
    if b == 1:
        return a
    else:
        c = a * a
        ans = fastpower(c, b / 2)

    if b % 2 == 1:
        return a * ans
    else:
        return ans


a, b = 5, 9
print fastpower(a, b), a**b
