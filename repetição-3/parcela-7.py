#8 - Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados:
#valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.
#Os juros e a quantidade de parcelas seguem a tabela abaixo:
#Qtd parcelas	% Juros sobre o valor inicial da dívida
#1	0
#3	10
#6	15
#9	20
#12	25
#Saída do programa
#Valor da Dívida - Valor dos Juros - Qtd de Parcelas - Valor da Parcela R$ 1.000 0 1 R$ 1.000,00 R$ 1.100 100 3 R$ 366,00 R$ 1.150 150 6 R$ 191,67
divida = int(input("digite o valor da divida"))
parcela = 1
juros = 0
print (f"{'parcelas':<20}  {'juros por parcela':<20} total por parcela")
for contador in range (5):
    jurosvalor= ((divida * juros)/parcela)
    if parcela < 3:
        parcela += 2
    elif parcela >= 3:
        parcela += 3
    if parcela == 3:
        juros = 0.1
    if parcela > 3:
        juros = juros + 0.05
    dividaparcela=divida//parcela
    print (f" {parcela:<20}{jurosvalor:<20} {dividaparcela}")