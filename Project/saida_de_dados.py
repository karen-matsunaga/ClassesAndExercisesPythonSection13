# print("Ola mundo")

# QUEBRA DE LINHA É PADRÃO
# print("Bom dia")
# print("Boa noite")

# SEM QUEBRA DE LINHA USANDO END
# print("Bom dia", end='')
# print("Boa noite")

# PRÁTICA NÃO RECOMENDADA, MAS FUNCIONA
# IMPRIMIR VALORES USANDO PLACEHOLDER
# x = "Maria"
# y = 19
# print("%s tem %d anos" % (x, y))

# IMPRIMIR VARIAVEL DENTRO DO PRINT
# x : int; y: int
# x = 10
# y = 20
# print(x)
# print(y)

# IMPRIMIR VALORES USANDO .FORMAT
# x: float
# x = 2.3456
# print("{:.2f}".format(x))

# IMPRIMIR VALORES USANDO INTERPOLAÇÃO
# idade: int
# salario: float
# nome: str; sexo: str
#
# idade = 32
# salario = 4560.9
# nome = "Maria Silva"
# sexo = "F"
#
# print(f"A funcionaria {nome}, sexo {sexo}, ganha {salario:.2f} e tem {idade} anos")

# PLACEHOLDER
# print("A funcionaria {:s}, sexo {:s}, ganha {:.2f} e tem {:d} anos".format(nome, sexo, salario, idade))

# PRÁTICA NÃO RECOMENDADA
# print("A funcionaria %s, sexo %s, ganha %.2f e tem %d anos" % (nome, sexo, salario, idade))