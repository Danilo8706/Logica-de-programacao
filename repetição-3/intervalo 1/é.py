#1-Ler 80 números e ao final informar quantos número(s) est(á)ão no intervalo entre 10 (inclusive)
#  e 150 (inclusive) 10 >= 150<=
total = 0
for intervalo in range (3):
    numero = int(input("digite numero"))
    if numero >= 10 and numero <= 150:
        total += 1
print (total,"numeros estão entre 10 e 150")