def fat(n):
    c = n
    f = 1
    for i in range (n, 0, -1):
        print('{} x'.format (c))
        f *= c
        c -= 1
        print(f)
fat(10)