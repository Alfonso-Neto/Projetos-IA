encomendas = []

def cadastro_encomendas():
    print('--- Cadastro de Encomendas ---')
    
    while True:
        try:
            qntd = int(input('Quantas encomendas você deseja registrar? (limite de 5 encomendas)? '))
            if qntd < 1:
                print('Você precisa digitar pelo menos 1 encomenda')
                continue
            elif qntd > 5:
                print('Você excedeu o limite de 5 encomendas!')
                continue
            else:
                break
        except ValueError: 
            print('Digite um número válido!')
    
    for i in range(qntd):
        encomenda = {}
        encomenda['id'] = input(f'Digite um identificador (alfanumérico) para a encomenda {i+1}: ')
        encomenda['eventos'] = []

        while True:
            try:
                etapas = int(input(f'Quantos eventos de rastreio haverá para a encomenda "{encomenda["id"]}"? '))
                if etapas < 1:
                    print('Você deve digitar ao menos 1 evento para a encomenda')
                else:
                    break
            except ValueError:
                print('Digite um número válido!')

        for j in range(etapas):
            evento = input(f'Digite o evento {j+1} da encomenda "{encomenda["id"]}": ')
            encomenda['eventos'].append(evento)

        encomendas.append(encomenda)


def mostrar_resumo():
    print('\n--- Resumo das Encomendas --- ')

    if not encomendas: 
        print('Nenhuma encomenda encontrada!')
        return
    
    for encomenda in encomendas: 
        print(f'Encomenda: {encomenda["id"]}')
        print('\n Eventos:')
        for i, evento in enumerate(encomenda['eventos'], start=1):
            print(f'{i}. {evento}')
        print('-' * 50)

cadastro_encomendas()
mostrar_resumo()