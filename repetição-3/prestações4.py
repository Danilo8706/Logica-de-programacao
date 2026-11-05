#Uma loja utiliza o código 1 para transação à vista e 2 para transação a prazo.
#  Faça um programa que receba o código e o valor de 15 transações.
#  Calcule e mostre: O valor total das compras à vistaO valor total as compras 
# a prazoO valor total das compras efetuadasO valor da primeira prestação das compras a prazo,
#  sabendo se que essas serão pagas em três vezes
somavalor = 0
avista = 0
aprazo = 0
for contador in range (5):
    valor = int(input("digite o valor da compra"))
    pagamento = input("o pagamento é avista ou aprazo?")
    somavalor = somavalor + valor
    if pagamento == "avista":
        avista = avista + valor
    elif pagamento == "aprazo":
        aprazo = aprazo + valor
print ("valor total de compras avista",avista)
print ("valor total de compras aprazo",aprazo)
print ("valor total ",somavalor)
print ("valor da primeira parcela aprazo",(aprazo /3))