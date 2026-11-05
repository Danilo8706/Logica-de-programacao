#8-	Peça ao usuário um número inteiro positivo e exiba todos os números pares
#  de forma decrescente até chegar a zero. O programa deve exibir a sequência 
numero = int(input("escreva o numero positivo"))
impar = 1
if numero % 2 != 0:
    numero = numero - impar
print (numero)
while numero >= 0:
    numero = numero -2
    print(numero)


