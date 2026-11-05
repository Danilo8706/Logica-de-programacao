#Crie um programa que simule uma calculadora simples.
#  O usuário deve informar a operação desejada e os dois
#  números para realizar o cálculo. As operações podem ser:
#  adição, subtração, multiplicação e divisão.
num1 = int(input("digite numero 1: "))
num2 = int(input("digite numero 2: "))
metodo = (input("qual metodo? adição,subtração.divisão ou multiplicação?"))
if metodo == "adição":
    print ("o resultado é",(num1 + num2))
elif metodo == "subtração":
        print ("o resultado é",(num1 - num2))
elif metodo == "divisão":
    print ("o resultado é",(num1 / num2))
else :
    print ("o resultado é",(num1 * num2))

