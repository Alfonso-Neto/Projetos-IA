#Crie um dicionario chamado cardapio, onde as chaves sao os nomes dos pratos e o valor sao  os preços. Faça o seguinte:
# Faça um laço para primeiro exibir o cardapio completo ao usuario 
# Crie um laço while para faer um menu de perguntas para coletar os pedidos.
# Pergunte ao usuário qual prato ele deseja
# Se o prato não estiver no dicionário, exiba "Prato indisponivel"
# Se estiver adicione na lista de pedidos
# Quando o usuario pedir para soar, mostra na tela o total do pedido dele.


cardapio = {

    "Gnocchi" : [25.0], 
    "Pizza" : [50.0],
    "Macarrão": [30.0]



}

pedidos = []

print('=' * 30)
print('\n CARDÁPIO: ')
for prato, preco in cardapio.items():
       print(f'{prato} R$ {preco}')

while True:

    opcao = input('Escolha uma das opções acima (ou digite sair para sair): ').title()
    print(opcao)
    if opcao.lower() == "Sair":
        break

    if opcao in cardapio:
         pedidos.append(cardapio[opcao])
         print(f'{opcao} adicionado ao pedido.')
    else:
         print('Prato não existe ou está indisponível.')

total = sum(cardapio)
print('Total do pedido: R$', total)

""" elif opcao.title() == "Gnocchi":
            print('Gnocchi anotado! ')
            pedidos.append(cardapio[opcao])
    elif opcao.title() == "Pizza":
            print('Pizza anotada! ')
            pedidos.append(cardapio[opcao])
    elif opcao.title() == "Macarrão":
            print('Macarrão anotado! ')
            pedidos.append(cardapio[opcao])
    elif opcao.title() == "Confirmar":
           print('Pedido anotado!' )
           break
    else:
            print('Desculpe, prato indisponível!')"""


