def somar():
    return valor_1 + valor_2

def multiplicar():
    return valor_1 * valor_2

def subtrair():
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


    if opcao == 1:
        valor_1 = float(input('Digite o primeiro valor: '))
        valor_2 = float(input('Digite o segundo valor: '))
        resultado = somar()
    elif opcao == 2: 
        valor_1 = float(input('Digite o primeiro valor: '))
        valor_2 = float(input('Digite o segundo valor: '))
        resultado = subtrair()
    elif opcao == 3:
        valor_1 = float(input('Digite o primeiro valor: '))
        valor_2 = float(input('Digite o segundo valor: '))
        resultado = dividir()
    elif opcao == 4:
        valor_1 = float(input('Digite o primeiro valor: '))
        valor_2 = float(input('Digite o segundo valor: '))
        resultado = multiplicar()
    else:
        print('Ops, opção inválida...')
        continue

    print(f'O resultado da equação é: {resultado}')


print('Saindo realmente do código agora!')