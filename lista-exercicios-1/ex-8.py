

a = 1
b = -1
c = -12

x1 = 0
x2 = 0

delta = 4 * a * c
delta = (b ** 2) - delta

raizDelta = delta ** (1/2)

parteBaixo = 2 * a

x1 = (-b + raizDelta) / parteBaixo
x2 = (-b - raizDelta) / parteBaixo

print("x1:", x1)
print("x2:", x2)