

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
    if op != 5:    
        n1 = int(input('Informe um número: '))
        n2 = int (input('Informe outro número: '))
    
        if op == 1:
            soma = n1 + n2
            print ('O resultado da soma é: ',soma)
        elif op == 2:
            subtração = n1 - n2
            print('O resultado da subitração é: ',subtração)
        elif op == 3:
            mult = n1 * n2
            print('O resultado da multiplicação é: ',mult)
        elif op == 4:
            div = n1 / n2
            print('O resultado da divisão é: ',div)
        elif op < 1:
            print('''Consagrado, eu desconheço verdadeiramente e me nego convincentemente a lhe dar uma saída relevante à essa sua entrada completamente confusa nesse universo de loucuragem, brigação e lutaria. Por obséquio, escolha uma opção válida do menu meu nobre!''')
        elif op > 5:
            print('''Consagrado, eu desconheço verdadeiramente e me nego convincentemente a lhe dar uma saída relevante à essa sua entrada completamente confusa nesse universo de loucuragem, brigação e lutaria. Por obséquio, escolha uma opção válida do menu meu nobre!''')
         

    