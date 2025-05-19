nomes = ["Ana", "Lucas", "Pedro", "João"]

for nome in nomes:
    if nome in ["João", "Ana"]:
        continue
    print("Chamando:", nome)