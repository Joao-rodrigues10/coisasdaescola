pessoas = ['diego', 'joao', 'jose', 'ronaldo']

print(pessoas[1])


pessoas2 = ['diego', 56748930]
nome, idade = pessoas2

print(pessoas2[0])
print(nome)

print(type(pessoas))

print(pessoas [1]) #retorna um indice

print(pessoas [-2])#retorna um indice de traz pra frente 

print(pessoas [1:])#retorna apartir do indice
print(pessoas [:3])#retorna de traz pra frete apartir do indice

print(pessoas [1:2])#retorna a partir do indice 1 até o 3 e exclui o 2,3

pessoas[3] = 'pedro'

print(pessoas)

pessoas.extend(['joao', 'maria', 'romeu', 'julieta'])#.extend inclui outra lista na lista atual

print(pessoas)

pessoas.append("ana")# põe uma pessoa no final da lista

print(pessoas)

pessoas.insert(2, 'ronaldo2')# inclui um registro, no local indicado
#primeiro argumento = indice
# segundo argumento = registro (dado)

pessoas.pop()#exclui o ultimo registro

pessoas.pop(4)#exclui o registro com o indice passado


pessoas.remove('romeu')
print(pessoas)

#pessoas.clear() # tira todo mundo da lista mas mantem a lista existindo

print(pessoas.index('joao'))#retorna em qual indice o registro esta (sendo o primeiro registro encontrado)

print(pessoas.count("maria"))
print(pessoas.count("joao"))

numeros = [33,25,60,10,20]

numeros.sort()

print(numeros)

numeros.reverse()

print(numeros)


maior_numero = max(numeros)

menor_numero = min(numeros)

print(maior_numero)

print(menor_numero)


turma = [
    ["joao", 20, 'desenvolvedor web'],
    ['maria', 19, 'desenvolvedora python'],
    ['romeu', 32, 'desenvolvedor PHP'],
    ['julieta', 31, 'desenvolvedora Flutter']
    ]

print(turma[3][1])

print(f'idade {turma[3] [1]} de {turma [3][0]}')

