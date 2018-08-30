with open("LyC_2018_2_Terminado/Tabla_de_simbolos.txt") as f:
    tabla = [[str(aaa) for aaa in line.split(';')] for line in f] #Convierte el texto a una Matriz
with open("LyC_2018_2_Terminado/codeone.txt") as f:
    code = list(f) # convierte el codigo a una lista

def arreglarStr (v):
    for i in range(len(v)-1):
        v[i][len(v[i])-1]= v[i][len(v[i])-1][:-1]

def arreglarStr2 (v):
        v[len(v)-1]+= "\n"

arreglarStr(tabla)
arreglarStr2(code)

def indexToken (v,string):
    for i in range (len(v)):
        if string == v[i][0]:
            return i
    return -1

operadortipo = []

def operatorSearch (i, j):
    if len(code[i])<2 or j==(len(code[i])-2):
        return False
    op = code[i][j]
    if buscarLista(operadores,op):
        op+= code[i][j+1]
        if buscarLista(operadores,op):
            operadortipo.append(op)
            return True
        else:
            op = op[:-1]
            operadortipo.append(op)
            return True
    else:
        return operatorSearch (i, j+1)


def analizadorOp (mop, i):
    if (i== len(code)):
        return mop
    else:
        if (operatorSearch(i,0)):
            mop.append(code[i])
        return analizadorOp (mop, i+1)

def crearMatrizOp ():
    mop=[]
    return analizadorOp(mop, 0)

matrizOperadores = crearMatrizOp()

for i in range(len(matrizOperadores)):
    print ("{0}    ||  Operador:   {1}    ||  Linea:  {2}".format(matrizOperadores[i],operadortipo[i],code.index(matrizOperadores[i])+1))
print ("\n\n\n\nTotal de operadores aritmeticos encontrados:  {0}".format(len(voperadores)))