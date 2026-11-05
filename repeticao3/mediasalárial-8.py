#Uma empresa utiliza os códigos 1 para funcionários do setor administrativo e
#2 para os funcionários do setor operacional. Faça um programa que receba o código
#e o salário de 20 funcionários. Calcule e mostre:
#A média salarial do setor administrativo.
#A média salarial do setor operacional.
#O total de salários pagos pela empresa.
#A quantidade de funcionários em cada setor.
import os
import time
somasalario = 0
mediaadm = 0
mediaopm = 0
adm = 0
opm = 0
salarioopm = 0
salarioadm = 0
qtd = 0
qtd2 = 0
for contador in range (4):
    codigo = int(input("digite o código do funcionário"))
    if codigo == 2:
        qtd2 +=1
        salarioopm = int(input("digite seu salário:\n"))
        print ("obrigado pela ajuda á pesquisa!")
        mediaopm =  qtd2/ salarioopm
        opm +=1
        time.sleep(0.5)
        os.system("cls")
    
    if codigo == 1:
        qtd +=1
        salarioadm = int(input("digite seu salário\n:"))
        print ("obrigado pela ajuda á pesquisa!")
        mediaadm =  qtd/ salarioadm
        adm += 1
        time.sleep(0.5)
        os.system("cls")
    somasalario = somasalario + salarioadm + salarioopm
print (f"a media salarial do setor administrativo é {mediaadm}")
print (f"a media salarial do setor operácional é {mediaopm}")
print (f"O total de salários pagos pela empresa é {somasalario}")
print (f"\nno setor administrativo contém um total de {adm} pessoas")
print (f"no setor operácional contém um total de {opm} pessoas")
