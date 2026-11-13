tempmax = 0
tempmin = 999999999
media = 0
for contador in range (3):
    temp = int(input("digite a temperatura"))
    if temp > tempmax:
        tempmax = temp
    if temp < tempmin:
        tempmin = temp
    media = temp + media 
print (f"a temperatura máxima foi {tempmax}")
print (f"a temperatura minima foi {tempmin}")
print (f"a média foi {media/(contador+1)}")