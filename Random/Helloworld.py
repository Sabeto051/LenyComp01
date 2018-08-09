file = open("LyC_2018_2_Terminado/Tabla_de_simbolos.txt")
tsim = [[str(aaa) for aaa in line.split(',')] for line in file] #Convierte el texto a una lista
file.close()

print (tsim[5] , "dddddd")