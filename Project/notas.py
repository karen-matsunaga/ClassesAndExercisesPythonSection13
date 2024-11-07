# EXERCÍCIO CORRETO - 1/10/24
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
nf = n1 + n2
print(f"NOTA FINAL = {nf:.1f}")
if nf < 60.0:
    print("REPROVADO")