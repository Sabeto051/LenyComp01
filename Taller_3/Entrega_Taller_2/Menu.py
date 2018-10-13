from os import sys
import AnalTablaSimbolos
import AnalTablaTokens
import AnalExpAritmet
url=""

def printTablaBonita(tabla):
    for i in tabla :
        row = ''
        for j in range(len(i)) :
            if j == 0 :
                a = 10
            elif j == 1 :
                a = 40
            else :
                a = 20
            
            a = a - len(i[j])
            while a >= 0 :
                i[j] += ' '
                a -= 1
            row += '|' + i[j] + '|'
        print (row)

def main():
    print ('=======================================')
    print ('=======================================')
    print ("Menú:")
    print ( "1) Ingresar dirreccion archivo .txt" )
    print ( "2) Analizador con tabla de símbolos" )
    print ( "3) Analizador con tabla de Tokens" )
    print ( "4) Identificador de expresiones aritmeticas" )
    print ( "5) Salir" )
    
    x = str (input ("Digite opción "))
    print ('=======================================')
    print ('=======================================')
    print ('\n\n\n\n')
    
    if (x== "1"):
        print ("Esta opción en mi codigo es inutil, \ncada opción lee el mismo archivo")
        print ('\n\n\n\n')
        input('Presiona Tecla Enter para volver al Menú')
        main()
    elif x=="2":
        tabla = AnalTablaSimbolos.crearMatrizTabla()
        # for i in tabla:
        #     print(i)
        printTablaBonita(tabla)
        input ("Presiona Tecla Enter para volver al Menú")
        print ('\n\n\n\n')
        main()
    elif x=="3":
        tabla = AnalTablaTokens.crearMatrizTabla()
        # for i in tabla:
        #     print(i)
        printTablaBonita(tabla)
        input ("Presiona Tecla Enter para volver al Menú")
        print ('\n\n\n\n')
        main()
    elif x=="4":
        tabla = AnalExpAritmet.crearMatrizTabla()
        for i in tabla:
            print(i)
        input ("Presiona Tecla Enter para volver al Menú")
        print ('\n\n\n\n')
        main()
    elif x=="5":
        sys.exit(0)

main()


