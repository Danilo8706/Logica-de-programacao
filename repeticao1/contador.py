somanota = 0.0
quantidadenota = int(input("quantas notas será digitado: "))
for contador in range (quantidadenota):
     nota = float (input("digite a nota"))
     somanota += nota
media = somanota / quantidadenota
print("sua média é: ", media)