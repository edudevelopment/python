A = int(input('Primeiro valor:'))
B = int(input('Segundo valor:'))
print('1 - adição')
print('2 - subtração')
print('3 - multiplicação')
print('4 - divisão')
operador = int(input('Qual seu operador:'))

if operador == 1:
    res = A + B
    print('Resultado: {} + {} = {}' .format(A, B, res))
elif operador == 2:
    res = A - B
    print('Resultado: {} - {} = {}' .format(A, B, res))
elif operador == 3:
    res = A * B
    print('Resultado: {} * {} = {}' .format(A, B, res))
elif operador == 4:
    res = A / B
    print('Resultado: {} / {} = {}' .format(A, B, res))
else:
    print('Operador invalido')

