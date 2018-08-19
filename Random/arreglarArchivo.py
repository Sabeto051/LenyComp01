with open('Random/Tabla_de_simbolos.txt') as file:
    tabla = [[str(element) for element in line.split(',')]for line in file]

tabla2 = ''.join([ ';'.join(line) for line in tabla]   )


with open ('Random/Tabla_de_simbolos2.txt', 'w') as file:
    file.write(tabla2)