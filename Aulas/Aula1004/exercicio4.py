# Contar vogais e consoantes de uma frase
# Ler uma frase do usuário
# Criar uma função usando um laço, conta vogais e quantas consoantes existem na frase.
# Desconsiderar caracteres que não são letras
# Dica: usar o char.isalpha() para verificar se os caracteres são letras

def contar_vogais_consoantes():
    #Conta o número de vogais e consoantes em uma frase, desconsiderando números, espaços e pontuação.
    
    vogais = "aeiouAEIOU"   #Define quais são as vogais
    quantidade_vogais = 0
    quantidade_consoantes = 0
 
    for char in frase:
        if char.isalpha():  
            if char in vogais:
                quantidade_vogais += 1
            else:
                quantidade_consoantes += 1
   
    return quantidade_vogais, quantidade_consoantes





frase = str(input("Digite uma frase: "))


quantidade_vogais, quantidade_consoantes = contar_vogais_consoantes(frase)
 

print(f"A quantidade de vogais nesta frase é de: {quantidade_vogais}")
print(f"A quantidade de consoantes nesta frase é de: {quantidade_consoantes}")
