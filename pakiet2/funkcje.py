def ca(a, r, n):
    i = 1
    while i < n:
        a+=r
        i+=1

    return a


def cg(a, q, n):
    i = 1
    while i < n:
        a *= q
        i += 1

    return a