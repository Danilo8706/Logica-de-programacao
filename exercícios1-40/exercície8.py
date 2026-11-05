#8.	Faça um programa que permita o cadastro de produtos em uma empresa.
#  O usuário deve informar o tipo de produto (Alimento, Bebida, Vestuário).
#  O programa deve exibir uma mensagem de confirmação com o tipo de produto
#  cadastrado e se ele é perecível ou não, de acordo com as seguintes regras:
# Alimento: Perecível 
# Bebida: Não Perecível 
# Vestuário: Não Perecível
produto = int(input("digite 1 para Alimento\n2 para bebida\n3 para vestuário"))
conf = int(input("digite 1 para conferir e 2 para não conferir"))
if conf == 1:
    if produto == 1:
        print ("alimento = Perecível")
    elif produto == 2:
        print ("bebida = não perecível")
    else :
        print ("vestuário = não perecível")
else :
    print ("produto não conferido")