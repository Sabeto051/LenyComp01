with open("LyC_2018_2_Terminado/Tabla_de_simbolos.txt", "r") as f:
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
        if string == v[i][0]:
            return i
    return -1

""" Creación de la Tabla de identificador de simbolos """

v = []
def addOperacion (i):
    string = ""
    for char in code[i]:
        if char == "\n" or char == "\t":
            1+1
        else:
            string += char
    v.append(string)



def analizadorLineas(i, j , matriz):
    
        char = code[i][j]
        if char == "\n":
            return matriz
        index = indexToken(tabla,char)
        if (index != -1): # si char es un token
            if ("Operador Aritmetico" in tabla[index][2]): # si char es op arit
                addOperacion(i)
                #
                char2 = code[i][j+1]
                index2 = indexToken(tabla,char+char2)
                if index2 != -1 : # char+char2 es operador
                    matriz.append(tabla[index2])
                    j+=1
                else : # char es operador de 1 caracter
                    matriz.append(tabla[index])
                return analizadorLineas(i,j+1, matriz)
        else: # char no es token
            return analizadorLineas(i,j+1, matriz)



def analizadorTokens(matriz,i):
    if i == len(code):
        return matriz
    else:
        matriz = analizadorLineas(i,0,matriz)
    return analizadorTokens(matriz,i+1)

def crearMatrizTabla():
    matriz = []
    return analizadorTokens(matriz,0)

resultado = crearMatrizTabla()

print(v)