# Calcule a média de notas digitadas pelo usuário.
# Pediar ao usuário quantas notas ele quer digitar
# Fazer um laço para pedir para inserir as notas
# Criar uma função de calcular a média
# Lembre de documentar a função 
# Faça um retorno duplo da função, um com a média e outro com a mensagem se aprovou ou não

def menu():
    """
    Exibe o menu principal com as opções disponíveis para o usuário.
    O menu permite o cadastro, edição, exclusão, exibição de contatos e a opção de sair.
    """
    print('\n MENU')
    print('-'*30)
    print('1 - Inserir notas')
    print('2 - Calcular média')
    print('3 - SAIR')

    opcao = input('Escolha uma das opções acima: ')

    return opcao



def notas_total():
    
    while True:
        quantidade = int(input('Quantas notas você deseja inserir (limite de 5 notas)? '))
        if quantidade <= 1:
            print('Você precisa digitar pelo menos 2 notas para calcular a média!')
            continue
        elif quantidade > 5:
            print('Você excedeu o limite de 5 notas para calculo de média!')
            continue
        else:
            break

    for i  in range(quantidade):
        while True:
            try:
              nota = float(input(f'Digite a nota {i+1} '))
              if  0 <= nota <= 10:
                    notas.append(nota)
                    break 
              else:
                    print('A nota deve ser entre 0 e 10!')
            except ValueError:
                print('Digite um número!')

def calcular_media(notas_total):

    media = sum(notas_total) / len(notas_total)

    if media >= 7:
        mensagem = "Aprovado"
    else:
        mensagem = "Reprovado"

    return media, mensagem

notas = []

while True:

    opcao = menu()

    if opcao == "3":
        print('Saindo...')
        break

    if opcao == "1":
        notas_total()
    elif opcao == "2":
        media, resultado = calcular_media(notas)
        print(f'Média: {media:.2f}')
        print(f'Resultado: {resultado}')
    else:
        print('Digite uma opcao válida!')
        continue