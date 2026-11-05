#7-	Crie um programa que solicite números ao usuário continuamente
#  até que ele insira um número negativo. Em seguida, exiba a média dos números positivos fornecidos.
numero = 0
soma = 0 
quantidade = 0
while numero >= 0:
    numero = int(input("escreva o numero"))
    if numero >= 0:
        soma += numero 
        quantidade += 1
    if numero > 0:
        media = soma / quantidade
         
print("sua média de numeros positivos é ",soma, "numeros positivos")

    