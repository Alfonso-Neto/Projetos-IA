def calcular_litros(km, consumo):
    """Calcula quantos litros serão necessários para a viagem"""
    return km / consumo

def calcular_custo_combustivel(litros, gasolina):
    """Calcula o custo total com combustível"""
    return litros * gasolina

def calcular_pdg(tem_pdg):
    """Calcula o custo com pedágios, se houver"""
    if tem_pdg:
        return float(input('Digite o valor total de pedágios: '))
    else:
        return 0.0
    
def mostrar(km, litros, custo_combustivel, custo_pdg):
    """Função que mostra o resumo e o custo da viagem"""
    valor_total =  custo_combustivel + custo_pdg
    print("\n----- CUSTO DA VIAGEM -----")
    print(f"Distância total: {km:.2f} km")
    print(f"Litros necessários: {litros:.2f} L")
    print(f"Custo com combustível: R$ {custo_combustivel:.2f}")
    print(f"Custo com pedágios: R$ {custo_pdg:.2f}")
    print(f"Custo total da viagem: R$ {valor_total:.2f}")


def menu():
    km = float(input('Digite quantos kilometros serão percorridos: '))
    consumo = float(input('Qual o consumo médio do carro? (KM/L) '))
    gasolina = float(input('Digite o preço atual do combustível: '))
    tem_pdg = input('Haverá pedágios? (S/N) ').lower() == 's'
           
    litros = calcular_litros(km, consumo)
    custo_combustivel = calcular_custo_combustivel(litros, gasolina)
    custo_pedagios = calcular_pdg(tem_pdg)

    mostrar(km, litros, custo_combustivel, custo_pedagios)

menu()