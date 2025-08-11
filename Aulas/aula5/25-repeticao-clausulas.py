numero = 0
soma = 0

while True:
    numero = int(input('Digite um numero ou digite 9999 para sair: '))
    if numero == 9999:
        break
    else:
        soma += numero
    # print(soma)

print('Fim')
print(soma)
