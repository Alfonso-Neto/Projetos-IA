def exibir_menu():
    print('\nMenu:')
    print('0 - Sair')
    print('1 - Fazer ação X')
    print('2 - Fazer ação Y')
    print('3 - Fazer ação Z')

    opcao = input('Digite a opção desejada: ')

    return opcao, "Usuário não digitou nada"

while True:
    opcao, mensagem = exibir_menu() 
    if opcao == '':
        print(f'Erro: {mensagem}')
        break

    if opcao == 0:
        break
