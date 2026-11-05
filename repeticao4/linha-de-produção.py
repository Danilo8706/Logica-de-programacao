#1- Balanceamento Dinâmico de Linha de Produção
#Uma linha tem 5 estações.
#Cada estação:
#Recebe peças
#Processa no máximo X por ciclo
#Pode quebrar se operar acima de 90% da capacidade por 5 ciclos seguidos
#Regras:
#Peças não processadas acumulam
#Se uma estação quebra:
#Toda a linha para
#Produção continua até:
#Meta diária atingida
#Ou falha estrutural
#Exibir:
#Produção total
#Estação que falhou (se houver)
#Ciclos executados
ciclo = 0
processados = 0
acima=0
contador = 0
processar = int(input("Digite a quantidade de peças que cada estação vai processar por ciclo: "))
meta = int(input("Digite a meta diária de produção: "))
capacidade = int(input("digite a capacidade da estação"))
capacidade90 = capacidade * 0.9
while True:
    ciclo += 1
    processados = processados + processar
    #processamento das peças
    if processar > capacidade90:
        contador +=1
        processar = capacidade
        processados = processados + processar
    else:
        contador = 0
    if contador == 5:
        print (f"total de peças processadas foi {processados}")
        print ("Estação quebrou")
        print (f"ciclos totais foram {ciclo}")
        break

    if processados >= meta:
        print("meta atingida")
        print (f"total de peças processadas foi {processados}")
        print (f"ciclos totais foram {ciclo}")
        break
    

