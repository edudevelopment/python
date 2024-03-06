print('Qual produto desejar comprar?')
print('1 - Maçã')
print('2 - Laranja')
print('3 - Banana')
produto = int(input('Qual sua escolha?'))
qtd = int(input('Qual a quantidade?'))
if(produto == 1):
    pagar = qtd * 3.6
    print('Voce comprou {} maças. Valor a pagar: {}' .format(qtd, pagar))
else:
    if(produto == 2):
        pagar = qtd * 2.8
        print('Voce comprou {} laranjas. Valor a pagar: {}'.format(qtd, pagar))
    else:
        if(produto == 3):
            pagar = qtd * 1.5
            print('Voce comprou {} bananas. Valor a pagar: {}'.format(qtd, pagar))
        else:
            print('Produto inexistente')