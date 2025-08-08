# Exercício: Criar um Conjunto
# Criando um conjunto chamado frutas = "maçã", "banana", "laranja"
# Saida Conjunto de frutas: [frutas]
 
# frutas = {"maçã", "banana", "laranja"}
# print(frutas)
 
 
 
 
# #############################################
 
# Exercício: Adicionar Elementos ao Conjunto
# Saida: Conjunto de frutas após adição: [frutas]
 
# frutas = {"maçã", "banana", "laranja"}
# frutas.add('uva')
# print(frutas)
 
 
##########################################################
 
# Exercício: Remover Elementos do Conjunto
# Removendo uma fruta do conjunto usando remove
# Saida: Conjunto de frutas após remoção: [frutas]
 
# frutas = {"maçã", "banana", "laranja"}
# frutas.remove("banana")
 
# print(frutas)
 
###############################################################
 
# Exercício: Verificar a Existência de um Elemento
# Verificando se a fruta 'laranja' está no conjunto
# Use a condicional if e else
# Saida verdadeira A fruta 'laranja' está no conjunto.
# Saida Falsa A fruta 'laranja' não está no conjunto.
 
# frutas = {"maçã", "banana", "laranja", "uva"}
 
# if 'laranja' in frutas:
#     print("A fruta 'laranja' está no conjunto.")
# else:
#     print("A fruta 'laranja' não está no conjunto.")
 
###########################################
 
# Exercício: Operações de União
# Criando outro conjunto de frutas
# frutas_citricas = "laranja", "limão", "tangerina"
# Saida: Todas as frutas: [todas_as_frutas]
 
# frutas = {"maçã", "banana", "uva"}
# frutas_citricas = {"laranja", "limão", "tangerina"}
# todas_as_frutas = frutas.union(frutas_citricas)
 
# print(todas_as_frutas)
 
###########################################
 
# Exercício: Operações de Interseção
# Criando um conjunto de frutas tropicais
# frutas_tropicais = "maçã", "banana", "coco"
# Encontrando a interseção entre os dois conjuntos usando .intersection
# Saida Frutas comuns: [frutas_comuns]
 
# frutas = {"maçã", "banana", "uva", "laranja"}
# frutas_tropicais = {"maçã", "banana", "coco"}
# frutas_comuns = frutas.intersection(frutas_tropicais)
 
# print(frutas_comuns)
 
# ########################################################
 
# Exercício: Diferença de Conjuntos
# Crie um conjunto de frutas de inverno
# frutas_inverno = "kiwi", "maçã", "pêra"
# Encontrando a diferença entre 'frutas' e 'frutas_inverno' usando .difference
# Saida Frutas que não estão no inverno: [frutas_diferentes]
 
# frutas = {"maçã", "banana", "uva", "laranja"}
# frutas_inverno = {"kiwi", "maçã", "pêra"}
# frutas_diferentes = frutas.difference(frutas_inverno)
 
# print(frutas_diferentes)
 
######################################################################
 
# Exercício: Conjunto de Elementos Únicos
# Crie uma lista com frutas repetidas
# lista_frutas = "maçã", "banana", "laranja", "maçã", "uva", "banana"
# Convertendo a lista em um conjunto para obter elementos únicos, usando o set()
# Saida: Frutas únicas: [frutas_unicas]
 
lista_frutas = ["maçã", "banana", "laranja", "maçã", "uva", "banana"]
frutas_unicas = set(lista_frutas)
 
print(frutas_unicas)
 
################################################################
 
# Exercício: Tamanho do Conjunto
# Crie um conjunto frutas "maçã", "banana", "laranja", "maçã", "uva"
# Obtendo o tamanho do conjunto de frutas, usando o len()
# Saida: O tamanho do conjunto de frutas é: [tamanho_frutas]
 
frutas = {"maçã", "banana", "laranja", "maçã", "uva"}
tamanho_conjunto_frutas = len(frutas)
 
print(tamanho_conjunto_frutas)
##############################################################
 
# Exercício: Limpar um Conjunto
# Crie um conjunto frutas "maçã", "banana", "laranja", "maçã", "uva"
# Limpando todos os elementos do conjunto, usando .clear()
# Saida: Conjunto de frutas após limpeza: frutas
 
frutas = {"maçã", "banana", "laranja", "maçã", "uva"}
 
print(frutas)
frutas.clear
print(frutas)

cor =('vermelho', 'verde', 'azul', 'amarelo', 'roxo')
primeira_cor = cor[0]
ultima_cor = cor[-1]

print(f'primeira cor : {primeira_cor}')

print(f'primeira cor : {ultima_cor}')
##############################################################


cor =('vermelho', 'verde', 'azul', 'amarelo', 'roxo')

cor_usuario = input("digite uma cor: ")

if 'azul' in cor:
    print(f"a cor {cor_usuario} esta na tupla. ")
else:
    print(f"a cor {cor_usuario} nao esta na tupla. ")

##############################################################


numeros = (3, 1, 2, 3, 4, 5, 2, 3)

contagem_dois = numeros.count(2)

print(f'o numero 2 aparece {contagem_dois} vezes na tupla.')
indice_tres = numeros.index(3)

print(f'o numero 3 esta no indice: {indice_tres} ')
##############################################################

tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6,)

tupla_contatenada = tupla1 + tupla2

print(tupla_contatenada)
##############################################################

tuplas_repetidas = ('a',) * 5

print(tuplas_repetidas)
##############################################################

lista_frutas = ['maça', 'banana', 'laranja']

print(lista_frutas)

tupla_frutas = tuple(lista_frutas)

print(tupla_frutas)
##############################################################


pessoa = ('joao', 30, 'programador')
nome, idade, profissao = pessoa 

#print(f'nome:'{nome}, 'idade:' {idade}, 'profissao:' {profissao})
##############################################################

tupla_aninhada = (
    ('maça' , 1)
    ('banana' , 2)
    ('laranja' , 3)
)

nome_banana = tupla_aninhada[1][0]
valor_banana = tupla_aninhada[1][1]

print(nome_banana)
print(valor_banana)


letras = ('a', 'b', 'c', 'd', 'e')
tamanho_tupla = len(letras)

print(f'o tamanho da tupla é: {tamanho_tupla}')




