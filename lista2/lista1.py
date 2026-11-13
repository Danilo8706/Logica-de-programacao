#1- Faça um algoritmo que leia a nota de 10 alunos de uma turma e guarde-as em um vetor. No final, mostre:
#a) Qual é a média da turma
#b) Quantos alunos estão acima da média da turma 
#c) Qual foi a maior nota digitada
#d) Em que posições a maior nota aparece
maiornota = 0
temporário = 0
lista = []
notaacima = 0
soma = 0
num = 0
posição = []
#fazendo lista
for contador in range (3):
    nota = int(input("digite sua nota"))
    soma = soma + nota
    lista.append(nota)

    #maior nota
    if nota > maiornota or contador == 0:
        maiornota = nota

    #achar posição maior nota


#média
media = soma / 3

#notas acima da média
for contador in range (3):
    if lista[contador] > media:
        notaacima +=1
    if lista[contador] == maiornota:
        posição.append(contador)
print(f"a média da turma é {media}")
print(f"{notaacima} alunos estão acima da média")
print(f"a maior nota foi {maiornota}")
print (f"a posição da maior nota foi {posição+1}")

