# Criar a lista com input
name = input("Write your name pls: ")
age = input("Write your age pls: ")
birthday = input("Write your birthday pls: ")

my_list = [name, age, birthday]

# Mostrar a lista
print("Sua lista atual:", my_list)

# Atualizar um item
index = int(input("Qual item deseja atualizar? (0 - name, 1 - age, 2 - birthday): "))
new_value = input("Digite o novo valor: ")

my_list[index] = new_value

# Mostrar a lista atualizada
print("Lista atualizada:", my_list)
