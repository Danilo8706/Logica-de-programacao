opcao = 1
contador = 0
while opcao >= 1:
    opcao = 0
    opcao = int(input("digite 1 para continuar: "))
    contador += 1
    temperatura = float(input("digite a temperatura"))
print ("saiu do sistema \n quantidade de vezes: ", contador, "\n ultima opção", opcao)