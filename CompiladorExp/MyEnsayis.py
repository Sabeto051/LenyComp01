numerosL = '1234567890'
letrasL = 'qwertyuiopasdfghjklñzxcvbnm'
terminalesL = '1234567890()+/-*'

finAnal = False
posicion = 0
TokenEntrada = ''
CadenaAnalizada = str(input( 'Ingrese cadena a Analizar: ' ))

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
            if not TokenEntrada in terminalesL :
                assert False , 'Error de Sintaxis con caracter : \'{0}\' en posición: {1}'.format(TokenEntrada, posicion-1)
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
            HacerMatch('*')
            Factor()
            TerminoPrima()
        else :
            pass            ## Epsilon

def Factor() :
    global finAnal, posicion
    if not finAnal :
        if TokenEntrada == '(' :
            HacerMatch('(')
            Expresion()
            HacerMatch(')')
        elif TokenEntrada in numerosL :
                Numero()
        else  :
            assert False , 'Error de Sintaxis con caracter : \'{0}\' en posición: {1} \n Se esperaba un digito'.format(TokenEntrada, posicion-1)
        # else :
        #     Numero()

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
        # else :
        #     assert False , 'Error de Sintaxis con caracter: \'{0}\' en posición: {1} \n Se esperaba un Dígito'.format(TokenEntrada, posicion-1)

def Digito() :
    global finAnal
    if not finAnal :
        global posicion
        if TokenEntrada in numerosL :
            HacerMatch(TokenEntrada)
        else :
            assert False , 'Error ...'

def HacerMatch(t) :
    global TokenEntrada
    if t == TokenEntrada :
        TokenEntrada = ObtenerToken()
    else :
        assert False, 'Error de Sintaxis con caracter: \'{0}\' en posición: {1} \n Se esperaba: \'{2}\' '.format(TokenEntrada, posicion-1,t)

def ObtenerToken() :
    global posicion, CadenaAnalizada, finAnal
    if posicion < len(CadenaAnalizada) :
        posicion = posicion + 1
        return CadenaAnalizada[ posicion -1 ]
    else :
        finAnal = True


def Principal() :
    global posicion, TokenEntrada
    posicion = 0
    TokenEntrada = ObtenerToken()
    Expresion()
    print ('Todo correcto, y yo que me alegro')

Principal()