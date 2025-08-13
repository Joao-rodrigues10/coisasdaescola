def exercicio1():
    i = 1
    while i <= 10:
        print(i)
        i += 1
    print("#" * 50)


def exercicio2():
    soma = 0
    i = 1
    while i <= 100:
        soma += i
        i += 1
    print("Soma:", soma)
    print("#" * 50)


def exercicio3():
    i = 1
    while i <= 10:
        print(f"5 x {i} = {5 * i}")
        i += 1
    print("#" * 50)


def exercicio4():
    i = 2
    while i <= 20:
        print(i)
        i += 2
    print("#" * 50)


def exercicio5():
    i = 1
    while i <= 10:
        print(f"{i} ao quadrado é {i ** 2}")
        i += 1
    print("#" * 50)


def exercicio6():
    i = 10
    while i >= 1:
        print(i)
        i -= 1
    print("#" * 50)


def exercicio7():
    i = 5
    resultado = 1
    while i > 0:
        resultado *= i
        i -= 1
    print(f"Fatorial de 5 é {resultado}")
    print("#" * 50)


def exercicio8():
    i = 1
    while i <= 20:
        if i % 2 != 0:
            print(i)
        i += 1
    print("#" * 50)


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
    print("#" * 50)


def exercicio10():
    lista_compras = []
    while True:
        item = input("Digite um item para adicionar à lista (ou 'sair' para terminar): ")
        if item.lower() == "sair":
            break
        lista_compras.append(item)
    print("Sua lista de compras é:")
    for produto in lista_compras:
        print("-", produto)
    print("#" * 50)


# Loop principal para permitir escolher múltiplos exercícios
while True:
    seletor = input("Insira o número do exercício (1 a 10) ou 'sair' para encerrar: ")
    if seletor.lower() == "sair":
        break

    if seletor.isdigit():
        seletor = int(seletor)
        if seletor == 1:
            exercicio1()
        elif seletor == 2:
            exercicio2()
        elif seletor == 3:
            exercicio3()
        elif seletor == 4:
            exercicio4()
        elif seletor == 5:
            exercicio5()
        elif seletor == 6:
            exercicio6()
        elif seletor == 7:
            exercicio7()
        elif seletor == 8:
            exercicio8()
        elif seletor == 9:
            exercicio9()
        elif seletor == 10:
            exercicio10()
        else:
            print("Número inválido, digite entre 1 e 10.")
    else:
        print("Entrada inválida. Digite um número ou 'sair'.")
