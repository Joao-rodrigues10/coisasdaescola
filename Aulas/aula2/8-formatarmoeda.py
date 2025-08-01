import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')


salario = 9999.99

salarioformatado = locale.currency(salario, grouping= True)

print(salario)

print(salarioformatado)