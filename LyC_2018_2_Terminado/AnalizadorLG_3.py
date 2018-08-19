with open("LyC_2018_2_Terminado/Tabla_de_simbolos.txt") as f:
    tabla = [[str(aaa) for aaa in line.split(',')] for line in f] #Convierte el texto a una lista
with open("LyC_2018_2_Terminado/codeone.txt") as f:
    code = list(f)

def arreglarStr (v):
    for i in range(len(v)-1):
        v[i][len(v[i])-1]= v[i][len(v[i])-1][:-1]

def arreglarStr2 (v):
        v[len(v)-1]+= "\n"

arreglarStr(tabla)
arreglarStr2(code)

def buscarLista (v, string):
    for i in range (len(v)):
        if string == v[i][0]:
            return True
    return False

def indexToken (v,string):
    for i in range (len(v)):
        if string == v[i][0]:
            return i
    return -1

""" Creación de la Tabla de identificador de toquens """



def AnalizadorLineas(i,j,string,separador,matriz):
    token = code[i][j]
    if token == "\n":
        return matriz

    if buscarLista(tabla,token): # Busca si el char es Separador u Operador
        k = indexToken(tabla,token)
        if tabla[ k ][2] == "Operador Aritmetico" or tabla [ k ][2] == "Operador Relacional":
            
            #Se "vacea" el acumulador string
            if string!="":
                if buscarLista(tabla,string):
                    h= indexToken(tabla,string)
                    matriz.append(tabla[h])
                else: 
                    newLine=[]
                    newLine.append(string)
                    newLine.append("Ladralo")
                    newLine.append("Identificador")
                    matriz.append(newLine)

            # Token es un Operador, y puede estar compuesto de 2 char
            token2 = tabla [i][j+1]
            if token2!="\n" and buscarLista(tabla,token+token2):
                #Se encotró un Operador de 2 char
                h= indexToken(tabla,token+token2)

                matriz.append(tabla[h])

                j +=1 # se acaban de poner 2 lineas en la matriz
                return AnalizadorLineas(i,j+1,"","",matriz)#######
            else:
                #Token no está compuesto de 2 char
                matriz.append(tabla[k])
                return AnalizadorLineas(i,j+1,"","",matriz)#######
        
        elif tabla [k][2] == "Separador":
            #Token es Separador

            if string!="":
                if buscarLista(tabla,string):
                    h= indexToken(tabla,string)
                    matriz.append(tabla[h])
                else: 
                    newLine=[]
                    newLine.append(string)
                    newLine.append("Ladralo2")
                    newLine.append("Identificador")
                    matriz.append(newLine)
            matriz.append(tabla[k]) #Se argega el separador
            return AnalizadorLineas(i,j+1,"","",matriz)#######"""

    
    else: #El token no se reconoce
        string+=token
        return AnalizadorLineas(i,j+1,string,separador,matriz)#######


                



    

def AnalizadorTokens(matriz,i):
    if i == len(code):
        return matriz
    else:
        string=""
        separador=""
        matriz = AnalizadorLineas(i,0,string,separador,matriz)
    return AnalizadorTokens(matriz,i+1)

def crearMatrizTabla():
    matriz = []
    return AnalizadorTokens(matriz,0)

resultado = crearMatrizTabla()

for a in resultado:
    print(a)