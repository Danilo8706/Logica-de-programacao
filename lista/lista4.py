lista =[]
cadastrar = 0
nome = 0
for contador in range(int(input("digite numero de vezes"))):
    contador +1
    print ("cadastrar nome = 1")
    print ("Pesquisar nome = 2")
    print ("Listar todos os nome  = 3")
    print ("sair do programa = 0")
    escolha = int(input("digite sua escolha"))
    if escolha == 1:
        cadastrar = input("cadastrar nome")
        lista.append(cadastrar)
    if escolha == 2:
        buscar = input("buscar nome")
        try: 
            nome = lista.index(buscar)
            print (f"o nome {buscar} está cadastrado no sistema na posição {nome} ")
        except:
            print ("nome não encontrado")
    if escolha == 3:
        print (f"a lista contém os nomes\n{lista}")
    if escolha == 0:
        break
