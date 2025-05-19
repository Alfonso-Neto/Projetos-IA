# Solicita que o usuário digite um número
numero = int(input("Digite um número: "))

# Verifica se o número é par ou ímpar usando o operador módulo (%)
if numero % 2 == 0:
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")