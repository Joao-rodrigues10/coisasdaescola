def fqnci_cliente():
    print("olá, você é um cliente frequente aqui na nossa loja?")
    rspt_cliente = str(input("sim/não: ").lower())
    semi_total = int(input("Digite o valor da sua compra: "))
    if semi_total >= 1000 or rspt_cliente == "sim":
        print("você tem um desconto de 15%😁")
    else:
        print("voce não tem desconto😭")



def verificação_numero():
    numero = int(input("Digite o numero para verificarmos: "))
    if numero >0:
        print("Este numero é positivo ")
    elif numero < 0 :
        print("Este numero é negativo")
    elif numero == 0:
        print("Este numero é zero 0 ")
    


def impar_par():

    num = int(input("Digite o número para verificarmos se é ímpar ou par: "))

    if num % 2 == 0 :
        print(f"O numero {num} é PAR 👍")
    else:
        print(f"O numero {num} é ÍMPAR 👍")




seletor = int(input("Para exiber Exercicios Insira: \n" \
"Exercicio 1 (1)\n" \
"Exercicio 2 (2)\n" \
"Exercicio 3 (3): "))

if seletor == 1:
    fqnci_cliente()
elif seletor == 2:
    verificação_numero()
elif seletor == 3:
    impar_par()
