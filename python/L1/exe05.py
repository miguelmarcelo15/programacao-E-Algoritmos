numero = int(input("fale um número de 1 a 10? "))
i = 1

while numero < 1 or numero > 10:
  numero = int (input ("seu número é invalido. tente novamente: "))
while i <= 10:
    print(numero, "x", i, "=", numero * i, "\n")
    i += 1

