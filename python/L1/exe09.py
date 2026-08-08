numero = int (input ("escreva um numero inteiro positivo: "))
i = 1
fatorial = 1


while (numero > 0 and i <= numero):
    fatorial = fatorial * i
    i += 1
print("o número ",numero, "em fatorial é : ",fatorial)


