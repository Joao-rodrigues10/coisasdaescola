def minha_funcao():
    print('Essa é minha função')

print('teste')
minha_funcao()
print('teste')


def menu_nome(nome):
    print(nome)

menu_nome('joão')
menu_nome('maria')


def menu_nome_idade(nome, idade, eh_verdade):
    print(nome, idade, eh_verdade)

menu_nome_idade('diego', 33, True)


def calculo_soma(num1, num2, num3):
    somar = num1 + num2 + num3
    print(somar)
    return somar  # Retornando para usar fora da função

numero1 = int(input('Digite um numero: '))
numero2 = int(input('Digite outro numero: '))
numero3 = int(input('Digite mais um numero: '))  # Adicionado terceiro número

calculo_soma(numero1, numero2, numero3)
calculo_soma(60, 5, 10)  # Adicionado terceiro número

# Exemplo de usar o valor retornado
resultado = calculo_soma(1, 2, 3)
print(resultado + 1)


def somar3(num1, num2):
    print('teste')
    return num1 + num2

print(somar3(5, 20))
