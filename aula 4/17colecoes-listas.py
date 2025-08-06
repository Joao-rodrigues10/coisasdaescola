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
