

def soma(n1,n2):
    s = n1 + n2
    print('O resultado da soma é: ',s) 
def sub(n1,n2):
    subt = n1 - n2
    print('O resultado da subitração é: ',subt)
def mult(n1,n2):
    m = n1 * n2
    print('O resultado da multiplicação é: ',m)
def div(n1,n2):
    d = n1 / n2
    print('O resultado da divisão é: ',d)

op = 0

while op != 5:
    print('''=========== < CALCULADORA MANEIRA > ===========:
[ 1 ] Somar dois números
[ 2 ] Subtrair dois números 
[ 3 ] Multiplicar dois números 
[ 4 ] Dividir dois números
[ 5 ] Sair''')
    op = int(input('Qual operação deseja realizar: '))
    if op == 5:
        print('Fim da operação.')
    if op >= 1 and op <= 4:    
        n1 = int(input('Informe um número: '))
        n2 = int (input('Informe outro número: '))
    
        if op == 1:
            soma (n1,n2)
        elif op == 2:
            sub(n1,n2)
        elif op == 3:
            mult(n1,n2)
        elif op == 4:
            div(n1,n2)
    else:
        print('''Consagrado, eu desconheço verdadeiramente e me nego convincentemente a lhe dar uma saída relevante à essa sua entrada completamente confusa nesse universo de loucuragem, brigação e lutaria. Por obséquio, escolha uma opção válida do menu meu nobre!''')
       