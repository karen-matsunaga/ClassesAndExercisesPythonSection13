# EXERCÍCIO CORRETO - 1/10/24
cod = int(input("Informe um codigo (1, 2, 3) ou 4 para parar: "))

alc, gas, die = 0, 0, 0
while cod != 4:
    if cod == 1:
        alc += 1
    elif cod == 2:
        gas += 1
    elif cod == 3:
        die += 1
    cod = int(input("Informe um codigo (1, 2, 3) ou 4 para parar: "))
print("MUITO OBRIGADO")
print(f"Alcool: {alc}\nGasolina: {gas}\nDiesel: {die}")