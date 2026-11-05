 #Faça um programa que leia o código dos itens pedidos e as
 #  quantidades desejadas. Calcule e mostre o valor a ser pago
 #  por item (preço *quantidade) e o total geral do pedido.
 #  Considere que o cliente deve informar quando o pedido deve ser encerrado.
       #"Especificação      Código     Preço
#        Cachorro Quente     100      R$ 1,20
 #       Bauru Simples       101      R$ 1,30
 #       Bauru com ovo       102      R$ 1,50
 #       Hambúrguer          103      R$ 1,20
  #      Cheeseburguer       104      R$ 1,30
  #      Refrigerante        105      R$ 1,00")
import os
import time
y = 0
precototal = 0
x = input("quer entrar no menu?\n sim ou não?")
x = x.lower()
if x in ("sim","si","s"):
    y = 1
    while y == 1 :
        os.system('cls' if os.name == 'nt' else 'clear')
        print ("Especificação      Código     Preço \nCachorro Quente     100      R$ 1,20 \nBauru Simples       101      R$ 1,30\nBauru com ovo       102      R$ 1,50\nHambúrguer          103      R$ 1,20\nCheeseburguer       104      R$ 1,30\nRefrigerante        105      R$ 1,00")
        opca = input("digite o codigo do lanche que deseja")
        if opca == "100":
            preco = 1.20
            precototal = precototal + preco
        elif opca == "101":
            preco = 1.30
            precototal = precototal + preco

        elif opca == "102":
            preco = 1.50
            precototal = precototal + preco
        elif opca == "103":
            preco = 1.20
            precototal = precototal + preco
        elif opca == "104":
            preco = 1.30
            precototal = precototal + preco
        elif opca == "105":
            preco = 1.00
            precototal = precototal + preco
        else:
            print ("error otário")
        print ("o preço do pedido é ", preco , "o preço total da compra é ", precototal)
        x = input("quer outro pedido? ?\n sim ou não?")
        x = x.lower()
        if x != "sim":
            y = 0
print (f"muito obrigado pela sua presença, o pedido deu um total de {precototal}")
        
