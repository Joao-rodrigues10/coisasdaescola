meses = {
    1 : 'janeiro',
    2 : 'fevereiro',
    3 : 'março',
    4 : 'abril',
    5 : 'maio',
    6 : 'junho'


}

print(meses)

print(type(meses))

print(meses[1])

meses = {

    'jan' : 'janeiro',
    'fev' : 'fevereiro',
    'mar' : 'março',
    'abr' : 'abril',
    'mai' : 'maio',
    'jun' : 'junho'


}

print(meses['abr'])

meses['jun'] = 'JUNHO'
print(meses)

meses['jul'] = 'JUlHO'
print(meses)

meses.pop('jan')

print(meses)


produtos = {
    'produto1':{
        'nome' : 'maça',
        'preco' :'6.50'
    },

    'produto2':{
        'nome' : 'banana',
        'preco' :'6.99'
    }
}

print(produtos['produto1']['nome'])
print(produtos['produto1']['preco'])

print(produtos['produto2']['nome'])
print(produtos['produto2']['preco'])


chaves = ['nome', 'idade', 'curso']

valores = ['diego', 33, 'python']

print(type(chaves))
print(type(valores))

pessoa = dict(zip(chaves, valores))

print(pessoa)
print(type(pessoa))


print(pessoa['nome'])

