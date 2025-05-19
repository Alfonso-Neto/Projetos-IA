valor = float(input("Informe o valor da compra: "))
desc = int(input("Qual o percentual de desconto para compra? "))
calcDesc = (valor - (desc/100)*valor)
print('O desconto aplicado ao produto é de: {}% Sendo o valor final = {}'.format(desc,calcDesc))