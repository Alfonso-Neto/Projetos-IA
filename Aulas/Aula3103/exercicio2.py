contador = 0 
lista = []

while True: 
    num = int(input('Digite um número: '))
    if num == 0:
        break
    contador += 1
    lista.append(num)

print(f'Foram digitados {contador} números e foram eles: {lista}')  