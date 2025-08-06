# Exercício: Criar e Exibir uma Lista
# Crie uma lista chamada frutas que contenha pelo menos 5 tipos de frutas.
# frutas = "maçã", "banana", "laranja", "uva", "kiwi"
# Exiba a lista de frutas na tela.
# Saida: Lista de frutas: [frutas]
 
 
# Exercício: Adicionar e Remover Elementos
# Adicione mais uma fruta à lista frutas criada no exercício anterior.
# Remova a primeira fruta da lista.
# Exiba a lista atualizada.
# Saida: Lista de frutas após adições e remoções: [frutas]
 
#######################################################################
 
# Exercício: Ordenar a Lista
# Crie uma nova lista chamada numeros com os números: 3, 1, 4, 1, 5, 9, 2, 6, 5.
# Ordene a lista numeros em ordem crescente.
# Exiba a lista ordenada.
# Saida: Lista de números ordenada: [numeros]
 
 
#######################################################################
 
# Exercício: Fatiamento de Listas
# Usando a lista numeros do exercício anterior, exiba os três primeiros números da lista.
# Exiba os números do meio (ou seja, exclua os primeiros e os últimos dois).
# Exibindo os três primeiros números da lista 'numeros'
# Saida 1: Três primeiros números: [3, 1, 4]
# Saida 2: Números do meio: [4, 1, 5, 9, 2]
 
#######################################################################
 
# Exercício: Encontrar o Maior e Menor Número
# Usando a lista numeros, encontre e exiba o maior e o menor número da lista.
# Encontrando o maior e o menor número na lista 'numeros'
# Saida 1:  Maior número: [maior_numero]
# Saida 2:  Menor número:: [menor_numero]
 
#######################################################################
 
# Exercício: Contar Elementos
# Crie uma lista chamada animais com os seguintes elementos: "gato", "cachorro", "pássaro", "gato", "peixe".
# Conte quantas vezes o "gato" aparece na lista e exiba o resultado.
# Saida: O 'gato' aparece [contagem_gato] vezes na lista.
 
 
#######################################################################
 
 
# Exercício: Remover Duplicatas
# Crie uma lista chamada itens com os seguintes elementos: ["maçã", "banana", "maçã", "laranja", "banana", "uva"].
# Crie uma nova lista que contenha apenas os itens únicos (sem duplicatas) e exiba essa lista.
# Saida: Itens únicos [itens]
######################################################################################
######################################################################################
######################################################################################
######################################################################################
def lista_frutas():
    frutas =['maçã', 'banana', 'laranja', 'uva', 'kiwi']

    print("lista de frutas", frutas)

    frutas.append('abacaxi')

    frutas.pop(0)

    print('lsta de frutas depois das adiçoes e remoçoes: ', frutas)
######################################################################################
def adicionar_remover():

    frutas = ["maçã", "banana", "laranja", "uva", "kiwi"]

    frutas.append("abacaxi")  

    frutas.pop(0)  

    print("Lista de frutas após adições e remoções:", frutas)
    ######################################################################################
def ordenar_numeros():
    num = [3, 1, 4, 1, 5, 9, 2, 6, 5]

    num.sort()

    print('çosta de numeros ordenada: ', num)
######################################################################################
def fatiamento():
    num = [3, 1, 4, 1, 5, 9, 2, 6, 5]

    num.sort()

    print("Tres primeiros numeros: ", num[:3])

    print("numero do meio: ", num[2:-2])
######################################################################################
def maior_menor():
     num = [3, 1, 4, 1, 5, 9, 2, 6, 5]

     print("maior numero", max(num))

     print("menor numero", min(num))

######################################################################################
def cortar_elementos():

    animais = ['gato', 'cachorro', 'passaro', 'gato', 'peixe']

    print(animais.count("gato"))
 ######################################################################################
def remover_duplicatas():

    itens = ["maçã", "banana", "maçã", "laranja", "banana", "uva"]

    itens_unicos = list(set(itens))

    print("Itens únicos:", itens_unicos)
######################################################################################

print("Bem Vindo, para ver exercicios insira: \n" \
      
"Exercicio 1 (1)\n" \
"Exercicio 2 (2)\n" \
"Exercicio 3 (3)\n" \
"Exercicio 4 (4)\n" \
"Exercicio 5 (5)\n" \
"Exercicio 6 (6)\n" \
"Exercicio 7 (7)\n" )
seletor = int(input("Insira o seletor: "))
if seletor == 1:
   lista_frutas()
elif seletor == 2:
   adicionar_remover()
elif seletor == 3:
   ordenar_numeros()
elif seletor == 4:
   fatiamento()
elif seletor == 5:
   maior_menor()
elif seletor == 6:
   cortar_elementos()
elif seletor == 7:
   remover_duplicatas()
else:
   print("Por favor digite um número valido")
 