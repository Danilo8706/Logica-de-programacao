#1- Faça um programa em Py que receba o total das vendas de cada vendedor e
#  armazenadas em um vetor. Receba também o percentual de comissão de cada 
# vendedor e armazene-os em outro vetor. Receba os nomes desses vendedores e
#  armazene ­os em um terceiro vetor. Existem apenas dez vendedores. Calcule
#  e mostre: 
nome =[]
comis = []
vendalista = []
vendas = 0
maiorvenda = 0
menorvenda = 99999999
posiçãomaior = 0
posiçãomenor = 0
for contador in range (2):
    
    
    nome.append(input("digite seu nome: "))
    comis.append(int(input("digite sua comissão: ")))
    venda = (int(input("digite valor da venda")))
    vendas += venda
    
    vendalista.append(int(venda))
    if maiorvenda < venda:
          maiorvenda = venda
          posiçãomaior = contador
    if menorvenda > venda:
              menorvenda = venda
              posiçãomenor = contador
print ("relatório")
for contador2 in range (2):
        
        print (f"\n{nome[contador2]} R${(comis[contador2]*vendalista[contador2])/100} ")
print (f"o total de vendas é R${vendas}")
print (f"a pessoa com a maior venda foi {nome[posiçãomaior]} com a venda de R${maiorvenda}")
print (f"a pessoa com a menor venda foi {nome[posiçãomenor]} com a venda de R${menorvenda}")

