def cadastrar_contato():
    """
    Solicita informações do usuário para criar um novo contato e adiciona essas informações a uma lista de contatos.
    O código do novo contato é determinado pelo índice da lista (ou seja, o tamanho da lista).
    As informações solicitadas incluem: nome, e-mail e telefone do contato.

    Exemplo de funcionamento:
    1. Solicita o nome, e-mail e telefone.
    2. Cria um dicionário com essas informações e o código do contato.
    3. Adiciona o dicionário à lista de contatos.
    """
    contato = {}
    contato["código"] = len(contatos)
    contato["nome"] = input('Digite o nome: ')
    contato["email"] = input('Digite o email: ')
    contato["telefone"] = input('Digite telefone: ')    
    contatos.append(contato)  
    print('Contato cadastrado com sucesso!!')


def editar():
    """
    Permite ao usuário editar um contato existente.
    O código do contato que o usuário deseja editar é solicitado, e caso o código seja válido,
    o nome, e-mail e telefone do contato podem ser modificados.

    Se não houver contatos cadastrados, exibe uma mensagem informando ao usuário.
    Caso o código fornecido seja inválido, exibe uma mensagem de erro.

    Exemplo de funcionamento:
    1. Exibe todos os contatos cadastrados.
    2. Solicita ao usuário o código do contato a ser editado.
    3. Permite editar nome, e-mail e telefone, caso o código seja válido.
    """
    if not contatos:
        print("Não existem contatos para editar!")
        return
    
    mostrar_contatos()

    codigo = int(input(f'Digite o código do contato que deseja editar:  '))
   
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


def deletar():
    """
    Permite ao usuário deletar um contato existente com base no código fornecido.
    Se não houver contatos cadastrados, exibe uma mensagem informando o usuário.
    Após a exclusão, os códigos dos contatos subsequentes são atualizados.
    
    Exemplo de funcionamento:
    1. Exibe todos os contatos cadastrados.
    2. Solicita ao usuário o código do contato a ser deletado.
    3. Deleta o contato da lista, atualizando os códigos dos contatos subsequentes.
    """
    if not contatos:
        print("Não existem contatos para deletar!")
        return
    
    mostrar_contatos()

    codigo = int(input(f'Digite o código do contato que deseja deletar: '))
 
    if codigo >= 0 and codigo < len(contatos):
        contatos.pop(codigo)

        # Atualiza os códigos dos contatos após a remoção
        for i in range(len(contatos)):
            contatos[i]["código"] = i

        print("Código deletado com sucesso!")
    else:
        print("Código inválido!")


def mostrar_contatos():
    """
    Exibe todos os contatos cadastrados na lista.
    Caso não haja contatos cadastrados, exibe uma mensagem informando ao usuário.
    """
    if contatos:
        print('\nLista de contatos:')
        for contato in contatos:
            print(f'Código: {contato["código"]} | nome: {contato["nome"]}, | Email: {contato["email"]} | Telefone: {contato["telefone"]}')
    else:
        print('Nenhum contato cadastrado')


def menu():
    """
    Exibe o menu principal com as opções disponíveis para o usuário.
    O menu permite o cadastro, edição, exclusão, exibição de contatos e a opção de sair.
    """
    print('\n MENU')
    print('-'*30)
    print('1 - Cadastro de contato')
    print('2 - Editar contato')
    print('3 - Deletar contato')
    print('4 - Mostrar todos os contatos')
    print('5 - SAIR')

    opcao = input('Escolha uma das opções acima: ')

    return opcao

# Lista de contatos
contatos = []

# Loop principal que mantém o programa em execução até o usuário escolher a opção de sair.
while True:
    
    opcao = menu()
   
    if opcao == "1":
        cadastrar_contato()
    elif opcao == "2":
        editar()
    elif opcao == "3":
        deletar()
    elif opcao == "4":
        mostrar_contatos()
    elif opcao == "5":
        print('Saindo...')
        break
    else:
        print('Tente novamente!')
