with open("Random/Tabla_de_simbolos2.txt", "r") as f:
    tabla = [[str(aaa) for aaa in line.split(';')] for line in f]


tablaf=[]

for i in tabla:
    tablaf.append(i[0])

with open("Random/Tabla_de_Tokens1.txt", "w") as f:
    j=1
    for i in tablaf:
        f.write(";"+str(j)+ ";"+str(i) + "\n")
        j+=1
    