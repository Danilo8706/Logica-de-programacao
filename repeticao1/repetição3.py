#3-	Fazer um programa que retorne quantos valores digitados pelo usuário são negativos.
#  Repetir o enquanto até o usuário digitar o valor ZERO:
contador = 0
numero = 1
while numero != 0:
    numero = int(input("digite o numero ou 0 para sair"))
    if  numero < 0:
       contador += 1    
print ("voce digitou: ",contador,"numeros negativos")