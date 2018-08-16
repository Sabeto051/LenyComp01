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

    if buscarLista(code,token): # Busca si el char es Separador u Operador
        k = indexToken(code,token)
        if code[ k ][2] == "Operador Aritmetico" or code [ k ][2] == "Operador Relacional":
            
            #Se "vacea" el acumulador string
            if string!= "":
                    newLine=[]
                    newLine.append(string)
                    newLine.append("Aún no se sabe la descripción")
                    newLine.append("Identificador")
                    matriz.append(newLine)

            # Token es un Operador, y puede estar compuesto de 2 char
            token2 = code [i][j+1]
            if token2!="\n" and buscarLista(code,token+token2):
                #Se encotró un Operador de 2 char
                h= indexToken(code,token+token2)

                matriz.append(code[h])

                j +=1 # se acaban de poner 2 lineas en la matriz
                AnalizadorLineas(i,j+1,"","",matriz)#######
            else:
                #Token no está compuesto de 2 char
                matriz.append(code[k])
                AnalizadorLineas(i,j+1,"","",matriz)#######
        
        else:
            #Token es Separador
            if token==".":
                separador=token # después de un punto va una función y antes, una clase
                if string!= "":
                    newLine=[]
                    newLine.append(string)
                    newLine.append("Clase - Objeto")
                    newLine.append("Identificador")
                    matriz.append(newLine)

                matriz.append(code[k]) # se pone el punto
                AnalizadorLineas(i,j+1,"",separador,matriz)#######
            
            elif token =="(":
                if separador==".":
                    #Entre el punto y el separador hay una función
                    if string!= "":
                        newLine=[]
                        newLine.append(string)
                        newLine.append("Función")
                        newLine.append("Identificador")
                        matriz.append(newLine)

                    matriz.append(code[k]) #Se argega el paréntesis
                    AnalizadorLineas(i,j+1,"","",matriz)#######
                    

                elif buscarLista(code,string):
                    #Si encuentra la string, simplemente la agrega a la matriz
                    matriz.append(code[ indexToken(code,string) ]) #Se agrega la string
                    matriz.append(code[k]) #Se argega el paréntesis
                    AnalizadorLineas(i,j+1,"","",matriz)#######
                
                else: 
                    if string!= "":
                        newLine=[]
                        newLine.append(string)
                        newLine.append("Función")
                        newLine.append("Identificador")
                        matriz.append(newLine)
                    matriz.append(code[k]) #Se argega el paréntesis
                    AnalizadorLineas(i,j+1,"","",matriz)#######
            
            elif token == "\"":
                if separador=="\"":
                    #Se tiene una string Constante, se agrega normalmente
                    if string!= "":
                        newLine=[]
                        newLine.append(string)
                        newLine.append("Cadena de caracteres")
                        newLine.append("Constante")
                        matriz.append(newLine)
                    matriz.append(code[k]) #Se argega la comilla
                    AnalizadorLineas(i,j+1,"","",matriz)#######
                elif separador=="":
                    if string!= "":
                        newLine=[]
                        newLine.append(string)
                        newLine.append("Ladralo")
                        newLine.append("NPI")
                        matriz.append(newLine)
                    matriz.append(code[k]) #Se argega la comilla
                    AnalizadorLineas(i,j+1,"","",matriz)#######
    
    else: #El token no se reconoce
        string+=token
        AnalizadorLineas(i,j+1,string,separador,matriz)#######


                



    

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
    matriz = AnalizadorTokens(matriz,0)
    return matriz

resultado = crearMatrizTabla()

for a in resultado:
    print(a)