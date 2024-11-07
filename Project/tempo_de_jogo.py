# EXERCÍCIO CORRETO - 1/10/24
hi = int(input("Hora inicial: "))
hf = int(input("Hora final: "))

if hi < hf:
    jogo = hf - hi
else:
    jogo = (24 - hi) + hf

print(f"O JOGO DUROU {jogo} HORA(S)")