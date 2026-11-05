2#Fazer um programa que calcule a tabuada de qualquer número
#, e o limite de cálculo deve ser definido pelo usuário:
tabuada = int(input("digite qual tabuada"))
limite = int(input("digite limite"))
contador = 0
while contador < limite:
   contador += tabuada
   print (contador)
