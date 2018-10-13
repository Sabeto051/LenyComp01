numerosL = '1234567890'
letrasL = 'qwertyuiopasdfghjklñzxcvbnmQWERTYUIOPASDFGHJKLÑZXCVBNM'
terminalesL = '1234567890()+/-*'

finAnal = False
posicion = 0
TokenEntrada = ''
# CadenaAnalizada = str(input( 'Ingrese cadena a Analizar: ' ))
CadenaAnalizada = ''

def Expresion() :
    global finAnal
    if not finAnal :
        Termino()
        ExpresionPrima()

def ExpresionPrima() :
    global finAnal
    if not finAnal :    
        if TokenEntrada == '+' :
            HacerMatch('+')
            Termino()
            ExpresionPrima()
        elif TokenEntrada == '-' :
            HacerMatch('-')
            Termino()
            ExpresionPrima()
        else :
            # if not TokenEntrada in terminalesL :
            #     assert False , 'Error de Sintaxis con caracter : \'{0}\' en posición: {1}'.format(TokenEntrada, posicion-1)
            pass            ## Epsilon

def Termino() :
    global finAnal
    if not finAnal :    
        Factor()
        TerminoPrima()

def TerminoPrima() :
    global finAnal
    if not finAnal :
        if TokenEntrada == '*' :
            HacerMatch('*')
            Factor()
            TerminoPrima()
        elif TokenEntrada == '/' :
            HacerMatch('/')
            Factor()
            TerminoPrima()
        else :
            pass            ## Epsilon

def Factor() :
    global finAnal, posicion, CadenaAnalizada
    if not finAnal :
        if TokenEntrada == '(' :
            HacerMatch('(')
            Expresion()
            HacerMatch(')')
        elif TokenEntrada in letrasL :
            Identificador()
        elif TokenEntrada in numerosL :
            Numero()
        else  :
            assert False , 'Error de Sintaxis en : \'{2}\', con caracter : \'{0}\' en posición: {1} \n Se esperaba un Dígito o Letra'.format(TokenEntrada, posicion-1, CadenaAnalizada)


def Numero() :
    global finAnal
    if not finAnal :
        Digito()
        NumeroPrima()

def NumeroPrima() :
    global finAnal, posicion
    if not finAnal :
        if TokenEntrada in numerosL :
            Digito()
            NumeroPrima()
        else :
            pass     ## Epsilon


def Digito() :
    global finAnal
    if not finAnal :
        global posicion
        if TokenEntrada in numerosL :
            HacerMatch(TokenEntrada)
        else :
            assert False , 'Error ...'

######################################

def Identificador() :
    global finAnal
    if not finAnal :
        if TokenEntrada in letrasL :
            Letra()
            CadenaLoN()


def Letra() :
    global finAnal, CadenaAnalizada
    if not finAnal :
        if TokenEntrada in letrasL :
            HacerMatch(TokenEntrada)
        else :
            assert False , 'Error de Sintaxis en : \'{2}\', con caracter : \'{0}\' en posición: {1} \n Se esperaba una Letra'.format(TokenEntrada, posicion-1, CadenaAnalizada)

def CadenaLoN() :
    global finAnal
    if not finAnal :
        if TokenEntrada in numerosL :
            Numero()
            CadenaLoNPrima()
        elif TokenEntrada in letrasL :
            CadenaLetras()
            CadenaLoNPrima()

def CadenaLoNPrima() :
    global finAnal
    if not finAnal :
        if TokenEntrada in letrasL :
            CadenaLetras()
            CadenaLoNPrima()
        elif TokenEntrada in numerosL :
            Numero()
            CadenaLoNPrima()
        else :
            pass        ## Epsilon

def CadenaLetras() :
    global finAnal
    if not finAnal :
        Letra()
        CadenaLetrasPrima()

def CadenaLetrasPrima() :
    global finAnal
    if not finAnal :
        if TokenEntrada in letrasL :
            Letra()
            CadenaLetrasPrima()
        else :
            pass        ## Epsilon


def HacerMatch(t) :
    global TokenEntrada, CadenaAnalizada
    if t == TokenEntrada :
        TokenEntrada = ObtenerToken()
    else :
        assert False, 'Error de Sintaxis en : \'{3}\', con caracter: \'{0}\' en posición: {1} \n Se esperaba: \'{2}\' '.format(TokenEntrada, posicion-1,t,CadenaAnalizada)

def ObtenerToken() :
    global posicion, CadenaAnalizada, finAnal
    if posicion < len(CadenaAnalizada) :
        posicion = posicion + 1
        return CadenaAnalizada[ posicion -1 ]
    else :
        finAnal = True

def OperacionAritmetica() :
    global CadenaAnalizada
    if '=' in CadenaAnalizada :
        if '+=' in CadenaAnalizada :
            Identificador()
            HacerMatch('+')
            HacerMatch('=')
            Expresion()
        elif '*=' in CadenaAnalizada :
            Identificador()
            HacerMatch('*')
            HacerMatch('=')
            Expresion()
        elif '-=' in CadenaAnalizada :
            Identificador()
            HacerMatch('-')
            HacerMatch('=')
            Expresion()
        else :
            Identificador()
            HacerMatch('=')
            Expresion()
    else :
        Expresion()

def Principal(cadena) :
    global posicion, TokenEntrada, finAnal, CadenaAnalizada
    posicion = 0
    CadenaAnalizada = cadena
    TokenEntrada = ObtenerToken()
    OperacionAritmetica()
    if finAnal == False :
        assert False, 'Error de Sintaxis con : \'{2}\', caracter: \'{0}\' en posición: {1} \n Se esperaba: un Dígito'.format(TokenEntrada, posicion-1, CadenaAnalizada)
    print ('Todo correcto, y yo que me alegro')

# Principal('veces54*=rRec34*4589-(4533/vve50)')