print("1-----------------------------------------------------------------------------------")
nome = input("Digite seu nome: ")
 
idade = input("Digite sua idade: ")
 
print(f'Olá,{nome}! Você tem {idade} anos')
 
print("2-----------------------------------------------------------------------------------")
nome_completo = "João Pedro"
 
idade = 17
 
salario_diario = 9999.99
 
print(f'Olá, meu nome é {nome_completo}, eu tenho {idade} anos de idade, atualmente trabalho como dono de uma empresa de cosmeticos e faço por dia {salario_diario:,.2f}')
 
print("3-----------------------------------------------------------------------------------")
 
num1 = int(input("digite seu primeiro numero inteiro: "))
 
num2 = int(input("digite seu segundo numero inteiro: "))
 
soma = num1 + num2
 
print(f'A soma dos numeros é : {soma}')
 
print("4-----------------------------------------------------------------------------------")
num = float(input("digite um numero decimal: "))
 
dobro = num * 2
 
print(f'O dobro do seu numero é {dobro}')
 
print("5-----------------------------------------------------------------------------------")
nome = input("Digite seu nome: ")
 
resposta = input("Você esta estudando atualmente? (sim/não): ").strip().lower()
 
esta_estudando = True if resposta == "sim" else False
 
print(f"{nome}, você está estudando: {esta_estudando}.")
 
if esta_estudando:
    print(f"{nome}, ótimo continue assim!")
else:
    print(f"{nome}, vamos estudar!")
 
print("6-----------------------------------------------------------------------------------")
nome = input("Digite seu nome: ")
 
quantidade = int(input("Digite um numero: "))
 
print((nome + '') * quantidade)
print("7-----------------------------------------------------------------------------------")
 
peso = float(input("Digite seu peso (kg): "))
 
altura = float(input("Digite sua altura (m): "))
 
imc = peso / (altura ** 2)
 
print(f"Seu IMC é: {imc:.2f}")
 
print("8-----------------------------------------------------------------------------------")
 
horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas: "))
 
valor_hora = float(input("Digite o valor da hora: "))
 
salario_bruto = horas_trabalhadas * valor_hora
 
print(f"Seu salário bruto é: R$ {salario_bruto:.2f}")
 
print("9-----------------------------------------------------------------------------------")
 
valor_produto = float(input("Digite o valor do produto: "))
 
porcentagem_desconto = float(input("Digite a porcentagem de desconto: "))
 
valor_desconto = valor_produto * (porcentagem_desconto / 100)
 
valor_final = valor_produto - valor_desconto
 
print(f"Valor final com desconto: R$ {valor_final:.2f}")