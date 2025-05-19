valor = float(input("Informe o valor da compra: "))

if valor >= 500:
    desconto = 0.30
elif valor >= 300:
    desconto = 0.2
elif valor >= 100:
    desconto = 0.1
else:
    desconto = 0
    print("Valor não tem desconto!")


valor_atualizado = valor - (valor*desconto)
print("Valor sem desconto:", valor)
print("Valor com desconto:", valor_atualizado)

"""
if valor >= 500:
    print('O desconto é de 30% =', valor - (0.30*valor))
elif valor >= 300:
    print('O desconto é de 20% =', valor - (0.20*valor))
elif valor >= 100:
    print('O desconto é de 10% =', valor - (0.10*valor))
else:
    print('Este valor não tem desconto!')


"""