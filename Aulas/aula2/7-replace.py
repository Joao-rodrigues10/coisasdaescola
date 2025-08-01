salario = 9999.999

print(salario)

salarioformatado = f'{salario:,.2f}'.replace('.','x').replace(',','.').replace('x',',')

print(f'R${salarioformatado}')

print(salarioformatado)

