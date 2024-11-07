# EXERCÍCIO CORRETO - 1/10/24
escala = input("Voce vai digitar a temperatura em qual escala (C/F)? ")

if escala == 'F':
    fah = float(input("Digite a temperatura em Fahrenheit: "))
    fah = (5 / 9) * (fah - 32)
    print(f"Temperatura equivalente em Celsius: {fah:.2f}")
elif escala == 'C':
    cel = float(input("Digite a temperatura em Celsius: "))
    cel = (9 / 5 * cel) + 32
    print(f"Temperatura equivalente em Fahrenheit {cel:.2f}")