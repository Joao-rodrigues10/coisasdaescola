#print('levantar')
#print('sair da mesa')

#print('passo 1')
#for passo in range(1, 10 + 1):
#print(f'passo {passo}')
#print("cheguei")
##########################################

#for passo in range(1, 10 + 1, 2):
#    print(f'passo {passo}')
#print("cheguei")

##########################################

#numero = int(input('digite um valor final : '))
#numero += 1 
#print(numero)

#for i in range(0, numero, 3):
#    print(i)
##########################################

#for i in range(0, numero, 3):
#    print(i)

#for i in range(20, 0, -1):
#    print(i)

# exercício: quatro valores pelo usuário, soma e resultado

# Inicializa a soma
soma = 0

for i in range(4):
    valor = int(input(f"Digite o {i+1}º valor: "))
    soma += valor

print("A soma dos valores é:", soma)


lista_nomes = ['diego', 'jeni', 'romeu', 'julieta', 'joao', 'gaby']

c = 0
for nome in lista_nomes:
    c += 1
    print(c, nome)


lista_pessoas = []

for i in range(2):
    nome = input('Digite um nome: ')
    lista_pessoas.append(nome)

print(lista_pessoas)


lista_produtos = {
    'computador': 4500.00,
    'impressora': 350.00,
    'teclado': 100.00
}

for produto, valor in lista_produtos.items():
    print(produto)
    print(valor)
    print(f'Produto {produto} custa R$ {valor:.2f}')

print("--- Usando keys ---")
for produto in lista_produtos.keys():
    print(produto)

print("--- Usando values ---")
for valor in lista_produtos.values():
    print(valor)
