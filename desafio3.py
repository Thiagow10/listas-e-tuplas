#Neste desafio foi proposto o seguinte cenário: Uma ONG está organizando uma campanha de arrecadação de alimentos e precisa registrar os nomes dos voluntários que vão ajudar na ação. À medida que os voluntários se inscrevem, seus nomes devem ser adicionados à lista e quando for digitado a palavra SAIR o programa deve encerrar.

lista_voluntários = []

while True:
    voluntario = input('Digite o nome do voluntário (ou SAIR para encerrar): ').strip()
    if voluntario == 'SAIR':
        break
    else:
        lista_voluntários.append(voluntario)

print(lista_voluntários)