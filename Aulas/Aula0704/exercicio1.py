def maior_num():
    """
    Função que verifica dois números e indica, entre os dois, qual é o maior.
    """
    if valor_1 > valor_2:
        print(f'O número {valor_1} é maior que o número {valor_2} ')
    elif valor_1 == valor_2:
        print('Os números são iguais!')
    else:
        print(f'O número {valor_2} é maior que o número {valor_1}' )
def entre():
    """
    Função que analisa 3 números, e diz, se o terceiro número está entre os dois primeiros.
    """
    if valor_3 in range(valor_1, valor_2):
        print(f'O número {valor_3} está entre {valor_1} e {valor_2}')
    else:
        print(f'O número {valor_3} não está entre {valor_1} e {valor_2}')
def entre_2():
    """
    Função que analisa 3 números, e diz, se o primeiro número está entre os dois últimos.
    """
    if valor_1 in range(valor_2, valor_3):
        print(f'O número {valor_1} está entre {valor_2} e {valor_3}')
    else:
        print(f'O número {valor_1} não está entre {valor_2} e {valor_3}')
        
while True:
    try:
        valor_1 = int(input('Digite um número: '))
        valor_2 = int(input('Digite um segundo número: '))
        valor_3 = int(input('Digite um terceiro número: '))
        
    except ValueError:
        print('Digite um valor válido!')
        continue

    maior_num()
    entre()
    entre_2()
    break
