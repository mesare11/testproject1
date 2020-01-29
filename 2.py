i=2000
mas=[i]
while (i<=7444443000):
    i=i+i//2 
    mas.append(i)
else:
    print(mas)
    print('Заражены все люди. На ' + str(len(mas)) + ' день наступил конец света')
