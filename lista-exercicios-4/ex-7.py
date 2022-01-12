
a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))

c = 0
i = b-a
for n in range(a,b):
    if n % 2 == 0:
        c += 1
    if i <= 15:
        print('{} '.format (n))    
if i > 15:
    print ('Meu nobre... tu informou números demais para eu lhe concedera dádiva de ver os pares do intervalo, mas posso te mostrar quantos pares ointervalo tem')
     
print('Existem {} números pares no intervalo informado '.format (c))
    