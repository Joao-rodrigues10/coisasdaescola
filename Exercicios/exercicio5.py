soma = 0

for i in range(4):
    valor = int(input("Digite o {}º valor: ".format(i+1)))
    soma += valor

print("A soma dos valores é:", soma)
