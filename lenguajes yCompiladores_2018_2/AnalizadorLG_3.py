file = open("lenguajes yCompiladores_2018_2/operadoresR.txt")
operadores = [[str(aaa) for aaa in line.split(',')] for line in file] #Convierte el texto a una lista
file.close()

def arreglarStr (v):
    for i in range(len(v)-1):
        v[i][len(v[i])-1]= v[i][len(v[i])-1][:-1]

def arreglarStr2 (v):
    for i in range(len(v)-1):
        v[i]= v[i][:-1]

