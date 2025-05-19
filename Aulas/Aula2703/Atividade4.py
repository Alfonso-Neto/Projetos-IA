#Dada uma string, percorra cada caractere com um laço for e conte quantas vogais (a, e, i, o, u)

frase = str(input("Digite uma frase: "))

contar = 0
for vogal in frase:
    if vogal in ('AaEeIiOoUu'):
        contar = contar + 1

    if contar == 0:
        print(f'Nessa frase não foi possível encontrar vogais')
        exit()

print(f'Nessa frase tem {contar} vogais')
