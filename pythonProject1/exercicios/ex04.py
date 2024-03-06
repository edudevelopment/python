nome = input('Qual seu nome?')
idade = int(input('Qual sua idade?'))
if (nome == 'Eduardo'):
    print('Olá Eduardo')
elif(idade < 18):
    print('Voce nao é o Eduardo, e é menor de idade')
elif(idade > 100):
    print('Diferente de Eduardo voce é imortal')
else:
    print('voce nao é o eduardo. se chama {} e tem {} anos' .format(nome,idade))
