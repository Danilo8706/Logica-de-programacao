#6-	Peça ao usuário para fornecer um número inicial e um intervalo.
#  Em seguida, faça uma contagem regressiva do número inicial até zero,
#  decrementando pelo intervalo especificado.intervalo=de numero em numero escolhido
numero = int(input("digite o numero"))
intervalo = int(input("digite o intervalo"))
while numero > 0:
    numero = numero -intervalo
    print(numero)
