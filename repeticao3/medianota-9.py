#Um professor registrou as notas de 35 alunos em uma prova. Faça um algoritmo que:
#Leia o nome e a nota de cada aluno.
#Informe a média geral da turma.
#Conte quantos alunos tiveram nota acima de 7.
nota = 0
medianota = 0
qtd = 0
somanota = 0
notamaior = 0
import os
import time
for contador in range (35):
    qtd +=1
    nome = input("digite seu nome")
    nota = round(input("digite sua nota"))
    
    time.sleep(2)
    os.system("cls")
    somanota = somanota + nota
    media = somanota / qtd
    if nota > 7:
        notamaior +=1
print (f"um total de {notamaior} alunos tiraram acima de 7")
print (f"a média da turma foi {media}")
