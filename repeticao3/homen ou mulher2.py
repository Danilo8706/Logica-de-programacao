#2 - Escrever um algoritmo que leia o nome e o sexo de 56 pessoas e informe
#  o nome e se ela é homem ou mulher. No final informe total de homens e de mulheres.
mulher= 0
homem = 0
for contador in range (5):
    nome = (input("escreva seu nome"))
    sexo = (input("escreva seu sexo(mulher ou homem)"))
    if sexo == "mulher":
        mulher += 1
    elif sexo == "homem":
        homem += 1
print ("na lista contém ",mulher," mulheres\n","na lista contém ",homem," homens")