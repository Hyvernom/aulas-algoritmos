
n = int(input("Digite um número: ")) 

if n > 10:
	print("“Meu Intel 2 cores não tankou o pancadão.")
else:
	c = n
	f = 1
	for i in range (n, 0, -1):
		print('{} x'.format (c))
		f *= c
		c -= 1
		print(f)
  