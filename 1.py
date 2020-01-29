humanPopulation=7444443000
currentInfected=2000
days=0
while (currentInfected<=humanPopulation):
currentInfected=currentInfected+currentInfected/2
days+=1 
print(format((currentInfected)) + ' людей поражено в день ' + str(days))
print('Заражены все люди. На ' + format(days) + ' день наступил конец света')
