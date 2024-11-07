# EXERCÍCIO CORRETO - 1/10/24
import math
a = float(input("Digite a medida A: "))
b = float(input("Digite a medida B: "))
c = float(input("Digite a medida C: "))
qua = math.pow(a, 2)
tri = (a * b) / 2
tra = (a + b) * c / 2
print(f"AREA DO QUADRADO = {qua:.4f}")
print(f"AREA DO TRIANGULO = {tri:.4f}")
print(f"AREA DO TRAPEZIO = {tra:.4f}")
