#A concessionária de veículos “CARANGO” está vendendo os seus
#  veículos com desconto. Faça um algoritmo que calcule e exiba
#  o valor do desconto e o valor a ser pago pelo cliente. O desconto
#  deverá ser calculado sobre o valor do veículo de acordo com o 
# combustível (álcool – 25%, gasolina – 21% ou diesel –14%).
carro = int(input("digite o valor do carro"))
combustivel = int(input("digite\n 1= gasolina\n2= diesel\n3= álcool"))
álcool = carro * 0.75
descontoA = carro *0.25
diesel = carro * 0.86
descontob = carro *0.14
gasolina = carro * 0.79
descontoc = carro * 0.21
if combustivel == 1:
  print ("o valor do seu carro é",gasolina, "o valor do desconto é",descontoc)
elif combustivel == 2:
  print ("o valor do seu carro é",diesel, "o valor do desconto é",descontob)
else :
  print ("o valor do seu carro é",álcool, "o valor do desconto é",descontoA)