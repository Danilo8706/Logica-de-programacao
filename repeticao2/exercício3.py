#João tem 1,50 metro e cresce 2 centímetros por ano, enquanto Zé tem 1,10
#metro e cresce 3 centímetros por ano. Construa um algoritmo que calcule e
#imprima quantos anos serão necessários para que Zé seja maior que João.
joão= 1.50
ze = 1.10
anos = 0
while joão > ze:
    ze += 0.03
    joão += 0.02
    anos +=1
print (anos)