#Neste desafio, foi proposto o seguinte cenário: Uma escola está organizando os dados dos alunos para criar um relatório resumido. Cada aluno tem seus dados registrados em uma única entrada, incluindo nome, idade e nota final no semestre.

entrada = input('Digite os dados do aluno no formato Nome, Idade, Nota separados por vírgula: ')
dados = entrada.split(', ')

for i in range(0, len(dados), 3):
    nome = dados[i]
    idade = int(dados[i+1])
    nota = float(dados[i+2])

    print(f'Aluno: {nome}')
    print(f'Idade: {idade}')
    print(f'Nota: {nota}\n')