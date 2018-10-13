with open("LyC_2018_2_Terminado/Tabla_de_Tokens.txt", "r") as f:
    tabla = [[str(aaa) for aaa in line.split(';')] for line in f] #Convierte el texto a una Matriz
with open("LyC_2018_2_Terminado/codeone.txt","r") as f:
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
        if string == v[i][2]:
            return i
    return -1

""" Creación de la Tabla de identificador de toquens """

def vaciarString(string , matriz):
    if string != "" : # si string no es vacía
            index = indexToken(tabla,string)
            if index != -1 : # string es token reconocible
                matriz.append(tabla[index])
            else: # string no se reconoce
                matriz.append(tabla[52])

def analizadorLineas(i, j , string, matriz):
    
        char = code[i][j]
        if char == "\n":
            return matriz
        index = indexToken(tabla,char)
        if (index != -1): # si char es un token
            if (index == 42 or index == 50): # si char es separador
                vaciarString(string, matriz)
                #
                return analizadorLineas(i,j+1, "" , matriz)
            else: # si char es token, pero toquen puede tener 2 chars
                vaciarString(string, matriz)
                #
                char2 = code[i][j+1]
                index2 = indexToken(tabla,char+char2)
                if index2 != -1 : # char+char2 es operador
                    matriz.append(tabla[index2])
                    j+=1
                else : # char es operador de 1 caracter
                    matriz.append(tabla[index])
                return analizadorLineas(i,j+1, "" , matriz)
        else: # char no es token
            string += char
            return analizadorLineas(i,j+1, string , matriz)



def analizadorTokens(matriz,i):
    if i == len(code):
        return matriz
    else:
        string=""
        matriz = analizadorLineas(i,0,string,matriz)
    return analizadorTokens(matriz,i+1)

def crearMatrizTabla():
    matriz = []
    return analizadorTokens(matriz,0)

resultado = crearMatrizTabla()

for a in resultado:
    print(a)