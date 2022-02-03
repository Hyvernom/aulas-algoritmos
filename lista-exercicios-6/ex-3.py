
def parImpar(n):
    r = n % 2

    if (r == 0):
        return('O número {} é PAR'.format(n))
    else:
        return('O número {} é ÍMPAR'.format(n))

p = parImpar(5)
print(p)