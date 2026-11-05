#2- Controle de Temperatura de Forno
#Um forno industrial inicia com temperatura informada pelo usuário.
#A cada ciclo:
#Se temperatura < 800 → aumenta 50 graus
#Se temperatura ≥ 800 e < 1000 → aumenta 20 graus
#Se temperatura ≥ 1000 → mantém constante
#O sistema deve repetir até:
#Atingir 1000 graus
#Exibir:
#Quantos ciclos foram necessários
#Temperatura final
ciclo = 0
temp = int(input("Digite a temperatura inicial do forno: "))
while True:
    ciclo +=1
    if temp < 800:
        temp += 50
    if temp >= 800 and temp < 1000:
        temp += 20
    if temp >= 1000:
        print (f"foram um total de {ciclo} ciclos")
        print (f"a temperatura final é {temp}")
        break