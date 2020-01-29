humanPopulation=7444443000
currentInfected=2000
allInfected=[currentInfected]
while (currentInfected<=humanPopulation):
    currentInfected=currentInfected+currentInfected//2 
    allInfected.append(currentInfected)
else:
    print(allInfected)
    print('Заражены все люди. На ' + format(len(allInfected)) + ' день наступил конец света')
