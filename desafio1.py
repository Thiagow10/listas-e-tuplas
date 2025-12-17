#Este desafio consiste em pedir ao usuário para consultar se o item já está na lista. Se não, o programa irá avisa-lo que o item precisa ser comprado

despensa = ['farinha', 'leite', 'ovos']

item = input('Digite o item que você quer verificar: ').lower()

if item not in despensa:
    print(f'O item {item} precisa ser comprado.')
else:
    print(f'O item {item} já está na despensa.')