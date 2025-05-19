#Peça ao usuário uma idade entre 0 e 120, enquanto for inválida, continue pedindo

while True:
    idade = int(input('Digite uma idade entre 0 e 120: '))
    if idade in range(0, 120):
        print('A idade foi registrada com sucesso')
        break
    else:
        print('Entrada inválida, tente novamente...')

print(f'Idade: {idade}')