listaimpar = []
listapar = []
contadorpar = 0
contadorimpar = 0
for contador in range(6):
    numero = int(input("digite o numero"))
    if numero %2 == 0:
        listapar.append(numero)
        contadorpar +=1
    if numero %2 != 0:
        listaimpar.append(numero)
        contadorimpar +=1
    
print(f"a quantidade de numeros pares é {contadorpar}")
print(f"os numeros pares são {listapar}")
print(f"a quantidade de numeros impares é {contadorimpar}")
print(f"os numeros impares são {listaimpar}")