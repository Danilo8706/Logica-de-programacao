#	Escreva um algoritmo que calcule a média dos números digitados pelo usuário
# , se eles forem pares. Termine a leitura se o usuário digitar zero (0).
par = 0
numero = 1
while numero != 0:
    numero = int(input("digite um numero maior que 0,se for zero o celular explode:"))
    if numero != 0:
        if numero % 2 == 0:
            par += 1
print ("voce digitou:",par," numeros positivos e o celular explodiu(voce morreu)")