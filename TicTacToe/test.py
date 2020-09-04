l = ['X', 'X', 'X', 
     'X', 'X', 'O',
     'O', 'X', 'O']

win = False

for i in range(0, 7, 3 ):
    linea = 0
    for j in range(i, 3 + i):
        if l[j] == 'X':
            linea += 1
        if linea == 3:
            win = True
            break

print(win)