#10-	Solicite ao usuário um número inteiro n e exiba uma estrutura em 
# forma de triângulo numérico de tamanho n. Cada linha do triângulo deve 
# conter números de 1 até o número da linha. Exemplo para 
n = int(input("escreva um numero"))
for contador in range (1, n +2):
        for coluna in  range (1,contador + 1 ):
            print (coluna, end=" ")  
        print()