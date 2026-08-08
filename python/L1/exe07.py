positivo = 0
negativo = 0
zero = 0
i = 1

while i <= 10:
    numero = int(input(f"Digite o {i}º número: "))

    if numero > 0:
        positivo += 1
    elif numero < 0:
        negativo += 1
    else:
        zero += 1

    i += 1

print("Positivos:", positivo)
print("Negativos:", negativo)
print("Zeros:", zero)
