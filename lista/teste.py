numero = []
while True:
    numero.append(input("digite seu texto"))

    print (numero)#escolhe posição da lista
    remover = input("quer remover um numero? \n1-sim\n2-não")
    if remover == 1 or remover == "sim":
        numero.remove(input("remova item"))
    elif remover != 1 or remover != "sim":
        print ("tabom")
    print (numero)
