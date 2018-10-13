tabla = [['Token 23','posicion : 342', 'SAntiago Bedoya'],['Token 2ee3','posicion : 3e242',' Marcela Bedoya'],['Token 2243','posicion : 3434',' SAntiago Cedoya']]

# row = ''
for i in tabla :
    row = ''
    for j in i :
        a = 25
        a = a - len (j)
        while a >= 0 :
            j += ' '
            a -= 1
        row += '|   ' + j + '|'
    print (row)
