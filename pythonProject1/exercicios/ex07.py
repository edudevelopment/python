lado1 = int(input('LADO 1:'))
lado2 = int(input('LADO 2:'))
lado3 = int(input('LADO 3:'))
if lado1 and lado2 and lado3 > 0:
    if(lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
        if lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
            print('triangulo escaleno')
        else:
            if lado1 == lado2 and lado1 == lado3:
                print('Triangulo equilatero')
            else:
                print('Triangulo isosceles')
    else:
        print('ao menos dos valores indicados nao servem para formar um triangulo')
else:
    print('ao menos dos valores indicados nao servem para formar um triangulo')

