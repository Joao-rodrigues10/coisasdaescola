# Exercício 1: Contagem de 1 a 10
# Imprima os números de 1 a 10.
 
#########################################################################
 
# Exercício 2: Soma dos Números
# Calcule a soma dos números de 1 a 100.
 
#########################################################################
 
# Exercício 3: Tabuada do 5
# Imprima a tabuada do 5.
 
#########################################################################
 
# Exercício 4: Números Pares
# Imprima todos os números pares de 1 a 20.
 
#########################################################################
 
# Exercício 5: Quadrados dos Números
# Imprima os quadrados dos números de 1 a 10.
 
#########################################################################
 
# Exercício 6: Contagem Regressiva
# Imprima uma contagem regressiva de 10 a 1.
 
#########################################################################
 
# Exercício 7: Fatorial de um Número
# Calcule e imprima o fatorial do número 5.
 
 
#########################################################################
 
# Exercício 8: Números Ímpares
# Imprima todos os números ímpares de 1 a 20.
 
 
#########################################################################
 
# Exercício 9: Contar Vogais
# Conte e imprima o número de vogais em uma string.
# string = "Hello, World!"
# vogais = "aeiouAEIOU"
 
#########################################################################
 
# Exercício 10: Gerenciador de Lista de Compras
# Peça ao usuário para adicionar itens à sua lista de compras até que ele digite "sair".
# Inicializa a lista de compras vazia
# Loop para adicionar itens
# Exibe a lista de compras com o loop FOR

def exercicio1():
    i = 1
    while i <= 10:
        print(i)
        i += 1
    print("####################################################")

def exercicio2():
    soma = 0
    i = 1
    while i <= 100:
        soma += i
        i += 1
    print("Soma:", soma)
    print("####################################################")

def exercicio3():
    i = 1
    while i <= 10:
        print(f"5 x {i} = {5*i}")
        i += 1
     print("####################################################")

def exercicio4():
    i = 2
    while i <= 20:
        print(i)
        i += 2
     print("####################################################")

def exercicio5():
    i = 1
    while i <= 10:
        print(f"{i} ao quadrado é {i**2}")
        i += 1
    print("####################################################")

def exercicio6():
    i = 10
    while i >= 0:
        print(i)
        i -= 1
    print("####################################################")


def exercicio7():
    i = 5
    resultado =1 
    while i <= 5:
        resultado*= i
        i+= 1 
    print(resultado)
    print("####################################################")


def exercicio8():
   i = 1
    while i <= 20:
        if i % 2 != 0:
            print(i)
        i += 1
    print("####################################################")

def exercicio9():
    string = "Hello, World!"
    vogais = "aeiouAEIOU"
    i = 0
    count = 0
    while i < len(string):
        if string[i] in vogais:
            count += 1
        i += 1
    print(f"Número de vogais na string '{string}': {count}")

