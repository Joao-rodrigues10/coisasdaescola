frutas = {'maça', 'laranja', 'abacaxi', 'banana' }


print(frutas)

print(type(frutas))


frutas.add("uva")

print(frutas)

frutas.remove('abacaxi')

print(frutas)


frutas.pop()
print(frutas)

outras_frutas = ('pera', 'banana')


frutas.update(outras_frutas)

print(frutas)

frutas_citricas = {'laranja', 'limao', 'tangerina', 'limao'}

todas_frutas = frutas.union(frutas_citricas)

print(todas_frutas)

print(frutas.intersection(todas_frutas))#teste


grupo_a = {'joao' , 'gaby'}

grupo_b = {'stella' , 'guilherme'}

uniao = grupo_a | grupo_b

print(uniao)

intersecao = grupo_a & grupo_b
print(intersecao)

diferencial = grupo_a - grupo_b
print(diferencial)
