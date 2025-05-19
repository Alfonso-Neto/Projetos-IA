# Crie um dicionario de alunos e suas notas. Faça um laço para verificar o seguinte:
# Se a nota é maior que 7, mostrar: "Fulano" foi aprovado.

alunos_notas = {
    "Ana": [9.0, 8.0, 2.0, 6.0],
    "Bruno": [6.5, 5.2, 3.5, 10.0],
    "Clara": [4.0, 3.0, 6.0, 10.0],
    "Diego": [2.0, 7.0, 9.0, 10.0],

}
for aluno, notas in alunos_notas.items():
    quantidade_de_notas = len(notas)
    total_das_notas = sum(notas)

    media = total_das_notas / quantidade_de_notas
    media = round(media, 2)
    
    if media >= 7: 
        print(f'{aluno} aprovado com média: {media}')
    elif 5 <=  media < 7:
        print(f'{aluno} em recuperação com média: {media}')
    else:
        print(f'{aluno} reprovado com média: {media}')