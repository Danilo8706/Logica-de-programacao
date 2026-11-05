#9.	Crie um programa que calcule o desconto a ser aplicado em uma compra.
#  O usuário deve informar o valor total da compra e o tipo de cliente 
# (Regular, VIP ou Funcionário). As regras para o desconto são:	VIP: 10% de desconto
# 	Funcionário: 20% de desconto regular: 0%
compra = int(input("escreva valor da compra"))
funcao = (input("escreva se é funcionario,vip ou regular: ")) 
if funcao == "funcionario":
    print ("o valor da compra é: ", (compra*0.80))
elif funcao == "vip" : 
    print ("o valor da compra é: ", (compra*0.10))
else : 
    print ("o valor da compra é: ", compra)
