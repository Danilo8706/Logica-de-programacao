peso = int(input("digite seu peso"))
planeta = int(input("digite 1 para Mercúrio:\n2 para vênus:\n3 para Marte:\n4 para júpiter:\n5 para saturno:\n6 para urano:\n"))
mercúrio = (peso/10)*0.37
vênus = (peso/10)*0.88 
marte = (peso/10)*0.38
jupiter = (peso/10)*2.64
saturno = (peso/10)*1.15
urano = (peso/10)*1.17
if planeta == 1:
     print ("seu peso em mercúrio é:" , mercúrio)
elif planeta == 2:
     print ("seu peso em vênus é:" , vênus)
elif planeta == 3:
     print ("seu peso em marte é:" , marte)
elif planeta == 4:
     print ("seu peso em júpiter é:" , jupiter)
elif planeta == 5:
     print ("seu peso em saturno é:" , saturno)
else :
     print ("seu peso em urano é:" , urano)