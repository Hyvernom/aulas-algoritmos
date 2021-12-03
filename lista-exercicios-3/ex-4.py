print('''Operações:
[ 1 ] somar
[ 2 ] subtrair 
[ 3 ] multiplicar 
[ 4 ] dividir''')
op = int(input('Qual operação deseja realizar: '))

n1 = int(input('Informe um número: '))
n2 = int (input('Informe outro número: '))

if (op == 1):
    soma = (n1 + n2)
    print ('O resultado da soma é: ',soma)
elif (op == 2):
    subtração = (n1 - n2)
    print('O resultado da subitração é: ',subtração)
elif (op == 3):
    mult = (n1 * n2)
    print('O resultado da multiplicação é: ',mult)
elif (op == 4):
    div = (n1 / n2)
    print('O resultado da divisão é: ',div)
elif (op >= 5):
    print('Opção invalida.')

    
       



