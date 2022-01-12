
n = int(input("Digite um número: ")) 
c = n
f = 1
if n > 10:
        print("“Meu Intel 2 cores não tankou o pancadão.")
if n <= 10:
        for i in range (n, 0, -1):
            print('{} x'.format (c))
            f *= c
            c -= 1
            print(f)
  