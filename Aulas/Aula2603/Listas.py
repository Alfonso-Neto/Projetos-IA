"""jogo = [ "League of Legends" , "World of Warcraft" , "Counter Strike" , "Valorant" , "Fortnite" ]
 
jogo_favorito = input("Digite o nome do seu jogo favorito: ")
 
for i, jogo in enumerate(jogo):
   
    if jogo.lower() == jogo_favorito.lower():
        posicao_jogo_favorito = i
        break
   
print(f"Seu jogo favorito está posição de indice {posicao_jogo_favorito} na lista de jogos.")"""







frutas = ["Goiaba", "Maça", "Laranja", "Banana", "Melao"]

frutafav = input('Qual sua fruta favorita: ')

for i, fruta in enumerate(frutas):
    
    if fruta.lower() == frutafav.lower():
        posicaofrutafav = i
        break
if posicaofrutafav is None:
    print('Minha fruta favorita não foi encontrada!')

print(f'Minha fruta favorita está na posição de indice {posicaofrutafav}.')