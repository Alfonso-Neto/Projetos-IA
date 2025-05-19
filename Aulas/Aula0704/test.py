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
def dividir(valor_1, valor_2):

    try:
        return valor_1 / valor_2
    except ZeroDivisionError:
        print('Não é possível dividir por zero!')
        return None
def menu():

    print('=' * 30)
    print('\nMenu da Calculadora')
    print('1 - Somar')
    print('2 - Subtrair')
    print('3 - Dividir')
    print('4 - Multiplicar')
    print('5 - Sair')
    while True:
        try:
            opcao = input('Que operação você deseja fazer? ')
            if opcao not in ["1", "2", "3", "4", "5"]:
                print('Opção inválida. Por favor, insira um número entre 1 e 5.')
                continue
            return opcao
        except ValueError:
            print('Você deve digitar um número válido (1-5)!')
 
while True:
    opcao = menu()
    if opcao == "5":
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
 
    funcao_escolhida = operacoes[opcao]
 
    resultado = aplicar_operacao(funcao_escolhida, valor_1, valor_2)
 
   
    if resultado is not None:
        print(f'Resultado: {resultado}')