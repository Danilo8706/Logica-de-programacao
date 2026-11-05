#Construa um algoritmo que receba o código de vários produtos e os
#  classifique de acordo com a tabela: CÓDIGO CLASSIFICAÇÃO 
# 1 Alimento não-perecível 
# 2 a 4 Alimento perecível
#5 e 6 Vestuário
#7 Higiene pessoal
#8 a 15 Limpeza e utensílios domésticos
#Qualquer outro código inválido exibe uma mensagem ao usuário.
#Quando o usuário digitar 0 (zero) o programa finaliza e exibe o número total
#de produtos classificados em cada categoria.
perecivel = 0
naoperecivel = 0
vestuario = 0
higiene = 0
limpesa = 0
while True:
    codigo = int(input("digite o codigo:\n1para não perecivel\n2 a 4 para perecivel\n5 a 6 para vestuário\n7 para higiene pessoal \n8 a 15 para limpeza,\nse for zero o programa para\n"))
    if codigo == 0:
        break
    if codigo == 1 :
         naoperecivel += 1
    elif codigo >= 2 and codigo <= 4:
        perecivel += 1
    elif codigo > 4 and codigo < 7:
        vestuario +=1
    elif codigo ==7 :
        higiene += 1
    elif codigo >= 8 and codigo <= 15:
        limpesa += 1
    else:
        print("CODIGOOO INVALIDOOOOO    ")
print ("------------------------------------------------------")
print ("voce comprou",perecivel,"itens pereciveis")
print ("voce comprou",naoperecivel,"itens não pereciveis")
print ("voce comprou",vestuario,"intens do vestuario")
print ("voce comprou",higiene,"itens de higiene")
print ("voce comprou",limpesa,"itens para limpeza")
print ("------------------------------------------------------")