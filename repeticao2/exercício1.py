
#Foram obtidos os seguintes dados:
# código da cidade
# número de veículos de passeio
# número de acidentes de trânsito com vítimas
#Deseja-se saber:
#a) o maior e o menor índice de acidentes de trânsito e a que cidades/estado pertencem
#b) qual a média de veículos nas cidades brasileiras (total / por estado)
#c) qual a média de acidentes com vítimas nas cidades de Santa Catarina e o total por estado.
maiorind = 0
menorind = 9999999
acidentessc = 0
vitimasc = 0
somaacidentesc = 0
somavitimasc = 0
mediaacidentessc = 0
somaacidenters = 0
somavitimars = 0
somavitimapr = 0
somaacidentepr = 0
maiorcidade = 0
codigomaior = 0
codigocidade1= ("sc")
codigocidade2= ("rs")
codigocidade3= ("pr")

for contador in range (3):
    codigo = int(input("escreva código da cidade:\n"))
    acidente = int(input("quantos acidentes teve?:\n"))
    vitima = int(input("quantas vitimas teve?:\n"))
       


    if codigo > 10 and codigo <15:
        somaacidentesc = somaacidentesc+acidente
        somavitimasc = somavitimasc+vitima
        if acidente > maiorind:
             maiorind = acidente
             codigomaior = codigocidade1  

    elif codigo > 20 and codigo <25:
        somaacidenters = somaacidenters+acidente
        somavitimars = somavitimars+vitima
        if acidente > maiorind:
            maiorind = acidente
            codigomaior = codigocidade2

    else :
        somaacidentepr = somaacidentepr+acidente
        somavitimapr = somavitimapr+vitima
        maiorind = acidente
        codigomaior = codigocidade3
   


print("maior indice é do estado" , codigomaior)






