#5- Cada espectador de um cinema respondeu a um questionário no qual constava sua idade e a sua opinião
#  em relação ao filme: ótimo=3, bom=2, regular=1. Faça um programa que receba a idade e a opinião de 15
#  espectadores e que calcule e mostre: (2 pontos)A média das idades das pessoas que responderam ótimoA 
# quantidade de pessoas que respondeu regularA percentagem de pessoas que respondeu bom entre todos os
#  espectadores analisados
media = 0
idadesoma = 0
qtd = 0
bom = 0
total = 0
regularqtd = 0
porcentagem = 0
import os
for intervalo in range (5):
    idade = int(input("digite sua idade"))
    nota = (input("digite \n1=regular\n2=bom\n3=ótimo"))
    total += 1
    if nota == "3":
        qtd += 1
        idadesoma = idadesoma + idade
        media = idadesoma / total
    elif nota == "1":
        regularqtd += 1
    elif nota == "2":
        bom += 1
        porcentagem = (bom/total) * 100
    os.system('cls' if os.name == 'nt' else 'clear')
os.system('cls' if os.name == 'nt' else 'clear')
print ("a media da idade das pessoas que responderam ótimo é",media)
print (regularqtd," pessoas escolheram regular")
print (porcentagem,"%" " é a porcentagem de pessoas que escolheram bom")