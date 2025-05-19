#Atualize o codigo anterior, some todos os numeros digitados
lista = []

while True: 
    num = int(input('Digite um número: '))
    if num == 0:
        break
    lista.append(num)
 
print(f'Foram digitados {len(lista)} números e foram eles: {lista}')  

listasum = sum(lista)

print(f'A soma desses números é: {listasum}')