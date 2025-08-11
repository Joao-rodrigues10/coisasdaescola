# 1. Exibir nome do aluno com f-string corretamente
aluno = {
    'nome': 'joao',
    'idade': 20,
    'curso': 'engenharia'
}

nome = aluno['nome']
print(f"Nome do aluno: {nome}")

##########################################################################

# 2. Atualizar e adicionar campos no dicionário
aluno = {
    'nome': 'joao',
    'idade': 20,
    'curso': 'engenharia'
}

print(aluno)

aluno['nota'] = 9.5
aluno['nome'] = 'diego'

print(aluno)

##########################################################################

# 3. Atualizar idade
aluno = {
    'nome': 'joao',
    'idade': 20,
    'curso': 'engenharia'
}

print(aluno)

aluno['idade'] = 21

print(aluno)

##########################################################################

# 4. Adicionar e remover chave com .pop()
aluno = {
    'nome': 'joao',
    'idade': 20,
    'curso': 'engenharia'
}

print(aluno)

aluno['nota'] = 9.5
print(aluno)

aluno.pop('nota')
print(aluno)

##########################################################################

# 5. Verificar se uma chave está no dicionário
aluno = {
    'nome': 'joao',
    'idade': 20,
    'curso': 'engenharia'
}

if 'curso' in aluno:
    print("O aluno está matriculado em um curso")
else:
    print("O aluno não está matriculado em um curso")

##########################################################################

# 6. Dicionário com dicionários (lista de alunos)
alunos = {
    'aluno1': {
        'nome': 'joao',
        'idade': 20,
    },
    'aluno2': {
        'nome': 'ronaldo',
        'idade': 99,
    }
}

print(f"Nome do segundo aluno: {alunos['aluno2']['nome']}")

##########################################################################

# 7. Criar dicionário usando zip
chaves = ['nome', 'idade', 'curso']
valores = ['carlos', 23, 'matematica']

dicionario_aluno = dict(zip(chaves, valores))
print(dicionario_aluno)

##########################################################################

# 8. Tamanho do dicionário
aluno = {
    'nome': 'joao',
    'idade': 20,
    'curso': 'engenharia'
}

tamanho_dicionario = len(aluno)

print(f"O tamanho do dicionário é: {tamanho_dicionario}")
