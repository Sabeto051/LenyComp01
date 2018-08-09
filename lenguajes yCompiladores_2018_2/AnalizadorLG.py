file = open("lenguajes yCompiladores_2018_2/palabrasreservadas.txt")
palres = list(file) #Convierte el texto a una lista
file.close()

file = open("lenguajes yCompiladores_2018_2/codeone.txt")
code = list(file)
file.close

def arreglarStr (v):
    for i in range(len(v)-1):
        v[i]= v[i][:-1]

arreglarStr(palres)
arreglarStr(code)

veces=[]
lineas=[]

for i in range (len(palres)):
    veces.append(0)
    lineas.append([])

for i in range(len(code)):
    string=""
    for j in range(len(code[i])):
        char = code[i][j]
        if (char!=" " and char!="(" and char!=":" ) and j!=len(code[i])-1 :
            string+= char
        else:
            if j==len(code[i])-1:
                string+=char

            comp= string in palres
            if comp==True:
                dank = palres.index(string)
                veces[dank]+=1
                lineas[dank].append(i+1)
            stirng=""

for i in range(len(veces)):
    print (str(palres[i]) + " = " + str(veces[i]) + " , Lineas: " + str(lineas[i]))
print("\n\n\n\n")
