file = open("lenguajesyCompiladores2018_2S/operadoresA.txt")
operadores = [[str(aaa) for aaa in line.split(',')] for line in file] #Convierte el texto a una lista
file.close()

file = open("lenguajesyCompiladores2018_2S/codeone.txt")
code = list(file)
file.close

def arreglarStr (v):
    for i in range(len(v)-1):
        v[i][len(v[i])-1]= v[i][len(v[i])-1][:-1]

def arreglarStr2 (v):
    for i in range(len(v)-1):
        v[i]= v[i][:-1]

def buscarLista (v, string):
    for i in range (len(v)):
        if string == v[i][0]:
            return True
    return False

arreglarStr(operadores)
arreglarStr2(code)

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

def sentenceSplit ():
    v=[]
    return sentenceSplitt(v, 0)

def sentenceSplitt (v, i):
    if (i== len(code)):
        return v
    else:
        if (operatorSearch(i,0)):
            v.append(code[i])
        return sentenceSplitt (v, i+1)

voperadores = sentenceSplit()

for i in range(len(voperadores)):
    #print(voperadores[i] + "    ||  Operador:   " + operadortipo[i] + "    ||  Linea:  "+ str(code.index(voperadores[i])+1 ) )
    print ("{0}    ||  Operador:   {1}    ||  Linea:  {2}".format(voperadores[i],operadortipo[i],code.index(voperadores[i])+1))
print ("\n\n\n\nTotal de operadores aritmeticos encontrados:  {0}".format(len(voperadores)))