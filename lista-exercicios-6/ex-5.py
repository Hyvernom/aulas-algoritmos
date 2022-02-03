
def imc(a,p):
    r = p/a

    return('Seu IMC é de: {}'.format(r))
a = float(input("Digite valor de A: "))
b = float(input("Digite valor de B: "))

x = imc(a,b)
print(x)