# EXERCÍCIO CORRETO - 1/10/24
import math

base = float(input("Base do retangulo: "))
altura = float(input("Altura do retangulo: "))
area = base * altura
perimetro = 2 * (base + altura)
diagonal =  math.sqrt(pow(altura, 2) + pow(base, 2))

print(f"AREA = {area:.4f}")
print(f"PERIMETRO = {perimetro:.4f}")
print(f"DIAGONAL = {diagonal:.4f}")
