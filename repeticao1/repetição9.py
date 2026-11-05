#9-	Crie um programa de adivinhação em que o computador escolhe aleatoriamente
#  um número entre 1 e 50, e o usuário precisa adivinhar. O programa deve fornecer 
# feedback (maior ou menor) a cada tentativa e permitir apenas 5 tentativas para
#  acertar. Se o usuário acertar antes do limite, exiba uma mensagem de vitória;
#  caso contrário, revele o número ao final.
import random
numero = random.randint (1,50)
errou = 0
for contador in range (5):
    num = int(input("escreva um numero de 1,50:\n"))
    if num == numero:
        print ("voce acertou:\n")
        errou = 1
        break
    elif num > numero:
        print ("digite um numero menor:\n")
    elif num < numero:
        print ("digite um numero maior:\n")
if errou == 0:
    print ("voce errou tudo burrooooooooo")
    
    

