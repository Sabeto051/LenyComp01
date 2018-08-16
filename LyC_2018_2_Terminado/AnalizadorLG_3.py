with open("LyC_2018_2_Terminado/Tabla_de_simbolos.txt") as f:
    tsim = [[str(aaa) for aaa in line.split(',')] for line in f] #Convierte el texto a una lista
with open("lenguajes yCompiladores_2018_2/codeone.txt") as f:
    code = list(f)

def arreglarStr (v):
    for i in range(len(v)-1):
        v[i][len(v[i])-1]= v[i][len(v[i])-1][:-1]

"""def arreglarStr2 (v):
    for i in range(len(v)-1):
        v[i]= v[i][:-1]"""

arreglarStr(tsim)
#arreglarStr2(code)

def buscarLista (v, string):
    for i in range (len(v)):
        if string == v[i][0]:
            return True
    return False

def indexi (v,string):
    for i in range (len(v)):
        if string == v[i][0]:
            return i
    return -1

for i in range(len(code)):
    string = ""
    for j in range(len(code[i])):
        char = code[i][j]