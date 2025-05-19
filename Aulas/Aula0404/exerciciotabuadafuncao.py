
def tabuada(numero):
    for i in range(1, 11):
        resultado = numero * i
        print(f'{numero} X {i} = {resultado}') 

tabuada(int(input('Digite um número para ver a tabuada: ')))
