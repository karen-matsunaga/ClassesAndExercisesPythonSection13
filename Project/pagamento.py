# EXERCÍCIO CORRETO - 1/10/24
nome = input("Nome: ")
vh = float(input("Valor por hora: "))
ht = int(input("Horas trabalhadas: "))
pag = vh * ht
print(f"O pagamento para {nome} deve ser {pag:.2f}")