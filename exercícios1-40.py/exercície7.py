#7.	Desenvolva um programa que analise o 
# desempenho de vendas de uma loja. O usuário
#  deve informar o total de vendas em um mês.
#  Com base no valor, o programa deve classificar
#  o desempenho de vendas:	Abaixo de R$ 5.000: 
# Desempenho Fraco	Entre R$ 5.000 e R$ 10.000: 
# Desempenho Regular	Acima de R$ 10.000: Desempenho Excelente
desempenho = int(input("escreva vendas totais"))
if desempenho < 5000:
    print ("desempenho fraco")
elif desempenho == 5000 and desempenho < 10001:
    print ("desempenho regular")
else :
        ("desempenho Excelente")
