listapar = []
listaimpar = []
numero = 0
while True:
    numero = (int(input("digite um numero")))
    if numero %2 == 0:
        listapar.append(numero)
    else:
        listaimpar.append(numero)
    if numero < 0:
        break
listapar.sort()
listaimpar.sort(reverse = True)
print(f"{listapar}")
print(f"{listaimpar}")