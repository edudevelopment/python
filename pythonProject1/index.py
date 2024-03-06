print('ola eduardo')

print(2 - 1)

print('2 + 3')

print('rafaela e' + ' eduardo')

print('o resultado da soma 2 + 5 é:', 2 + 5)


nota = 8.5
disciplina = 'Logica de programação'

print(nota)
print(disciplina)

a = 5
b = 3
resposta = a != b
print(resposta)

frase = 'ola mundo'
print(frase[4])


s1 = 'logica de programaçao'
s1 = s1 + ' e algoritmos'
print(s1)

s2 = 'A' + '-' * 10 + 'B'
print(s2)

s3 = 'Voce tirou %f na disciplina de algoritmos' % nota
print(s3)

s4 = 'Voce tirou %.2f na disciplina de algoritmos' % nota
print(s4)

dis = 'programaçao'
s5 = 'voce tirou %.1f na disciplina de %s' % (nota, dis)
print(s5)

s6 = 'voce tirou {} na disciplina de {}' .format(nota, dis)
tamanho = len(s6)
print(tamanho)
print(s6)
print(s6[0:10])
print(s6[:5])