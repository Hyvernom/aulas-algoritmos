
print('|||========== CALCULADORA DE BHASKARA ==========|||')

a = float(input('Informe o valor de a: '))
b = float(input('Informe o valor de b: '))
c = float(input('Informe o valor de c: '))

x1 = 0
x2 = 0

delta = (b ** 2) - (4 * a * c)
raizDelta = delta ** (1/2)

x1 = (-b - raizDelta) / (2 * a)
x2 = (-b + raizDelta) / (2 * a)

print("x1 =", x1)
print("x2 =", x2)