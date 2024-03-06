print('Qual seu produto?')
print('1 - Maçã')
print('2 - Laranja')
print('3 - Banana')
produto = int(input('Qual sua escolha?'))
if(produto > 3):
    print('Produto inexistente')
qtd = int(input('Qual a quantidade?'))
if(produto == 1):
    pagar = qtd * 3
    print('Voce comprou {} maças. Valor a pagar: {}' .format(qtd, pagar))
elif(produto == 2):
    pagar = qtd * 2.5
    print('Voce comprou {} laranjas. Valor a pagar: {}' .format(qtd, pagar))
elif(produto == 3):
    pagar = qtd * 1.5
    print('Voce comprou {} bananas. Valor a pagar: {}' .format(qtd, pagar))

