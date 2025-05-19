#banco

saldo = 2000
while True:
    print('=' * 30)
    print('\n Menu do Banco')
    print('1 - Consulta de Saldo')
    print('2 - Depositar Saldo')
    print('3 - Saque Saldo')
    print('4 - Sair')
    opcao = input('Escolha uma das opções acima: ')
    print('=' * 30)
    if opcao == "1":
        
        print(f'O seu saldo é de: R${saldo}')
    elif opcao == "2":
        try:
            deposito = float(input('Qual o valor a ser depositado? '))
        except:
            print("Não foi digitado um número")
            continue

        saldo = saldo + deposito 
        print(f'O saldo após o depósito é de: R${saldo}')    
    elif opcao == "3":        
        saque = float(input('Qual o valor a ser sacado? '))
        saldo = saldo - saque
        print(f'O saldo após o saque é de: R${saldo}')
    elif opcao == "4":        
        print('Saindo...')
        break
    else:
        print('Opção invalida... Tente novamente')

