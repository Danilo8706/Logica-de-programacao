#4-	A prefeitura de uma cidade fez uma pesquisa entre seus habitantes,
#  coletando dados sobre o número de filhos e salário. A prefeitura deseja saber:  
# a) média do salário da população; 
#b) média do número de filhos; 
#) maior salário; 
#d) percentual de pessoas com salário até R$100,00. 
#O final da leitura de dados se dará com a entrada de um salário negativo.  
mediasalário = 0
salario = 0
mediafilhos = 0
filhos = 0
salario100 = 0
qntd = 0
somasalario = 0
somafilhos = 0
maiorsalario = 0
salario100p = 0
while salario >= 0: 
    filhos  = int(input("escreva quantidade de filhos\n"))
    salario = float(input("escreva qual seu salário\n"))
    qntd += 1
    if salario > 0 :
     somasalario += salario
     somafilhos += filhos
    if salario > maiorsalario:
       maiorsalario = salario
       if salario <= 100:
          salario100 += 1
print ("a media de salario da população é:\n",somasalario/(qntd-1),
                "\na media de numero de filhos é:\n",somafilhos/(qntd-1),"\no maior salário da média de salários é:\n"
                    ,maiorsalario,"\no percentual de pessoas com salário abaixo de 100 é:",((salario100*100) / qntd))
 
