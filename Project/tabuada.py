# EXERCÍCIO CORRETO - 1/10/24
n = int(input("Deseja a tabuada para qual valor? "))

for i in range(1, 11):
    prod = n * i
    print(f"{n} x {i} = {prod}")