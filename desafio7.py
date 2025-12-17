#Neste desafio foi proposto o seguinte cenário: O clube de atletismo Alura Runners organizou uma corrida e divulgou a lista com a classificação final dos participantes. Mas, um erro foi identificado: um dos nomes está incorreto. O organizador precisa de um programa que permita localizar o nome errado e substituí-lo pelo correto.

lista_nomes = ['Ana', 'Carlos', 'Pedro']

nome_incorreto = input('Digite o nome incorreto: ')
nome_correto = input('Digite o nome correto: ')

if nome_incorreto in lista_nomes:
    lista_nomes.remove(nome_incorreto)
    lista_nomes.insert(1, nome_correto)
    print(f'O nome {nome_incorreto} foi substituido por {nome_correto}.')
    print('Lista atualizada: ', lista_nomes)

else:
    print('Nome não encontrado.')