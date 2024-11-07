# EXERCÍCIO CORRETO - 1/10/24
print("Digite as idades: ")
idade = int(input())

cont, soma, med = 0, 0, 0
if idade < 0:
   cont = 1
   print("IMPOSSIVEL CALCULAR")
else:
   while idade >= 0:
       if cont == 0:
           soma = soma + idade
           cont += 1
       elif cont > 0 and idade > 0:
           soma = soma + idade
           cont += 1
       idade = int(input())

   med = soma / cont
   print(f"MEDIA = {med:.2f}")