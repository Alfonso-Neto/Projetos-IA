
while True:
    try:
        numero = int(input('Digite um numero: '))
        print('Resultado', 10 / numero)
        break
    except ZeroDivisionError:
        print('Não pode dividir por zero!')
    except ValueError:
        print('Valor digitado não é um número inteiro!')
    except Exception as erro:
        print('Ops, ocorreu um erro!', erro)