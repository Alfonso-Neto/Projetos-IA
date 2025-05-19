#Crie uma lista vazia chamada contatos e faça um laço para iterar sobre um menu, com estas tres opções: 
# Criar um menu com as seguites opções:
# Opção 1: cadastro de um novo contato. solicitar a digitação das informações: código(deverá ser o índice da lista), nome, e-mail, telefone
# Opção 2: Editar um contato. Solicitar qual código deseja acessar para então permitir editar os valores daquele contato.
# Opção 3: Deletar um contato. Solicitar qual código deseja acessar para então permitir apagar e então remove-lo da lista.
# Opção 4: Mostar todos os contatos 
contatos = []

while True:
    print('\n MENU')
    print('-'*30)
    print('1 - Cadastro de contato')
    print('2 - Editar contato')
    print('3 - Deletar contato')
    print('4 - Mostrar todos os contatos')
    print('5 - SAIR')
    opcao = int(input('Escolha uma das opções acima: '))
    if opcao == 1:
       contato = {}
       contato["código"] = len(contatos) 
       contato["nome"] = input('Digite o nome: ')
       contato["email"] = input('Digite o email: ')
       contato["telefone"] = input('Digite telefone: ')     
       contatos.append(contato)  
       print('Contato cadastrado com sucesso!!')
        
    elif opcao == 2:
        codigo = int(input('Digite o código do contato que deseja editar: '))
    
        if codigo >= 0 and codigo < len(contatos):
            print('Contato atual:', contatos[codigo])
            nome = input('Digite o novo nome(ou deixe em branco para manter o mesmo): ')
            email = input('Digite o novo email(ou deixe em branco para manter o mesmo): ')
            telefone = input('Digite o novo telefone(ou deixe em branco para manter o mesmo): ')

            if nome:
                contatos[codigo]['nome'] = nome
            if email:
                contatos[codigo]['email'] = email
            if telefone:
                contatos[codigo]['telefone'] = telefone

            print('Contato atualizado com sucesso!')            
        else:
            print('Código inválido')
    elif opcao == 3:
        codigo = int(input('Digite o código do contato que deseja deletar: '))

        if codigo >= 0 and codigo <len (contato):
            contato.pop(codigo)

            for i in range(len(contatos)):
                contatos[i]["codigo"] = i 
                
            print("Código deletado com sucesso!") 
        else:
            print("Código inválido!")   

    elif opcao == 4:
        if contatos:
            print('\n')
            print('Lista de contatos:')
            for contato in contatos:
                print(f'O nome é: {contato["nome"]}, \n Email: {contato["email"]} \n Telefone: {contato["telefone"]}')
        else:
                print('Nenhum contato cadastrado')

    elif opcao == 5:
        print('Saindo...')
        break
    else:
        print('Tente novamente!')