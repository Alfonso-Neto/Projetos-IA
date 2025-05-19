def aplicar_operacao(operacao, valor_1, valor_2):
    """
    Função de alta ordem que recebe dois valores e uma função chamada de operação. Aplica a operação
    e retorna o resultado dela.
    """
    return operacao(valor_1, valor_2)

def somar(valor_1, valor_2):
    """
    1° Explicar a função
    2° Explicar os parâmetros
    3° Explicar os retornos    
    """

    return valor_1 + valor_2

def multiplicar(valor_1, valor_2):
    return valor_1 * valor_2

def subtrair(valor_1, valor_2):
    return valor_1 - valor_2

def dividir():
    try:
        return valor_1 / valor_2
    except ZeroDivisionError:
        print('Não é possivel dividir por zero!')

def menu():
    
    print('=' * 30)
    print('\n Menu da Calculadora')
    print('1 - Somar')
    print('2 - Subtrair')
    print('3 - Dividir')
    print('4 - Multiplicar')
    print('5 - Sair')
    try:
        opcao = int(input('Que operação você deseja fazer? '))
    except:
        print('Você deve digitar uma opção válida!')
        return None
    
    return opcao
    
while True: 
    
    opcao = menu()

    if opcao == 5: 
        print('Saindo...')
        break
    try:
        valor_1 = float(input('Digite o primeiro valor: '))
        valor_2 = float(input('Digite o segundo valor: '))
    except ValueError:
        print('Não é um número válido. Tente novamente.')
        continue

    operacoes = {
        "1": somar,
        "2": subtrair,
        "3": dividir,
        "4": multiplicar,

    }
    
    if opcao in operacoes:
        funcao_escolhida = operacoes[opcao]

        resultado = aplicar_operacao(funcao_escolhida)

        print(f'Resultado {resultado}')
    else:
        print('Opção inválida. Tente novamente!')

