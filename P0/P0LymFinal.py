"""P0 - LYM
Nombre: Mariana Forero Ávila
Correo: m.foreroa@uniandes.edu.co

Nombre: Lina María Gomez Mesa
Correo: l.gomez1@uniandes.edu.co"""

"""Imports de librerías"""
import sys  # se importa sys para poder usar sys.exit()

"""Definición de parámetros GLOBALES"""

variables_globales = []  # se generan variables globales para poder usarlas en el resto del programa
dic_PROC = {}  # Diccionario que guarda los nombres de las funciones y la cantidad de sus parámetros
direcciones = ["left", "right", "around"]  # direcciones
orientaciones = ["north", "south", "east", "west"]  # lista de orientaciones
ins = ["walk", "jump", "grab", "pop", "pick", "free", "drop"]  # lista de instrucciones
comandos = ["walk", "jump", "jumpTo", "veer", "look", "drop", "grab", "get", "free", "pop"]  # lista de comandos

"""Definición de CASOS"""


def caso1(linea, variables):  # n
    """:param linea: 1 línea del archivo .txt :param variables: lista de variables locales"""
    var = linea.split("(")  # Se separa la linea por el caracter (
    par = var[1].strip(")")  # Se quita el caracter ) de la linea
    if len(var[1].split(",")) > 1:  # Si la longitud de la lista es mayor a 1
        abort()
    elif par.isnumeric() is False:  # no es un número se verifica que es variable o parámetro
        isVar(variables, par)  # Si no aborta el proceso continúa


def caso2(linea, lista):
    """:param linea: 1 línea del archivo .txt :param lista: lista de variables locales"""

    var = linea.split("(")  # Se separa la linea por el caracter (
    paras = var[1].strip(")").replace(" ", "").split(",")  # Se quita el caracter ) de la linea y se separa por comas
    if not len(var[1].split(",")) == 2:  # Se comprueba que la longitud de la lista es 2
        abort()  # Si len(var[1].split(",")) es diferente de 2 aborta el programa
    else:
        for p in paras:  # Se recorre la lista de parámetros
            if p.isnumeric() is False:  # Si no es un número se verifica que es variable o parámetro
                isVar(lista, p)


def caso3(linea):
    """ :param linea: 1 línea del archivo .txt """
    var = linea.split("(")  # Se separa la linea por el caracter (
    par = var[1].strip(")")  # Se quita el caracter ) de la linea
    if not len(var[1].split(",")) == 1:  # Se comprueba que la longitud de la lista es 1
        abort()  # Si len(var[1].split(",")) es diferente de 1 aborta el programa
    elif par.isnumeric():
        abort()  # Si es un número aborta el programa
    elif var[0] == "veer":
        is_dir(par)  # Si var[0] es veer se verifica que par sea una dirección
    elif var[0] == "look":
        is_orie(par)  # Si var[0] es look se verifica que par sea una orientación


def is_orie(linea):
    """ :param linea: 1 línea del archivo .txt """
    if linea not in orientaciones:  # Se comprueba que la orientación sea correcta con la lista de orientaciones
        abort()


def is_dir(linea):
    """ :param linea: 1 línea del archivo .txt """
    if linea not in direcciones:  # Se comprueba que la dirección sea correcta con la lista de direcciones
        abort()


def isVar(lista, var):
    """ :param lista: lista de variables locales :param var: variable a verificar"""
    if lista is not None:  # Si la lista no está vacía
        if var not in lista:  # Se comprueba que la variable exista en la lista de variables locales
            if var not in variables_globales:
                abort()  # Si no existe en variables globales aborta el programa
    else:
        if var not in variables_globales:
            abort()  # Si no existe en variables globales aborta el programa


"""DEFINICIONES SECUNDARIAS"""


# Maneja decir que el programa es erróneo
def abort():  # se aborta el programa
    print("NO")
    sys.exit()


# Maneja la primer línea de PROC
def primeralproc(linea1):
    """ :param linea1: primera línea de PROC """
    linea = linea1.replace("\n", "")  # Se quita el salto de línea
    variables_locales = []  # Se crea una lista de variables locales
    proc = linea.replace(" ", "").replace("\n", "").removeprefix("PROC").split("(")  # se quita PROC y se separa por (
    if len(proc) == 1 or linea.endswith(")") is False or len(proc[1].removesuffix(")").split(",")) - 1 != proc[1].count(",") or len(proc[0]) == 0:  # Se comprueba que los prámetros se encuentren dentro del paréntesis
        abort()
    else:
        dic_PROC[proc[0]] = len(proc[1].split(","))  # Se extrae el nombre de la función y se mete por si se utiliza luego
        if len(proc[1].split(",")) > 1:  # Se comprueba que la longitud de la lista de parámetros sea mayor a 1
            for x in proc[1].removesuffix(")").split(","):
                if x.isalnum() and x[0].isalpha():  # Comprueba parámetros sean alfanuméricos y que empiecen por letra
                    variables_locales.append(x)  # Se añaden a la lista de variables locales
                else:
                    abort()  # Si no se cumple la condición aborta el programa

    return variables_locales  # Se devuelve la lista de variables locales


"""Estructuras de control"""


# Maneja condicionales de if
def metodo_if(linea, variables_loc):
    """ :param linea: 1 línea del archivo .txt :param variables_loc: lista de variables locales """
    lineac = linea.removeprefix("if").removesuffix("fi")  # Se quita el if y el fi
    if not linea.endswith("fi"):  # Se comprueba que termine con fi
        abort()  # Si no se cumple la condición aborta el programa
    elif "else" in lineac:
        elseDef(lineac, variables_loc)  # Si se encuentra el else se ejecuta la función elseDef
    else:
        ifNormal(lineac, variables_loc)  # Si no se encuentra el else se ejecuta la función ifNormal


# Maneja if sencillo (una condicion y un bloque)
def ifNormal(lineac, variables_loc):
    """ :param lineac: 1 línea del archivo .txt :param variables_loc: lista de variables locales """
    vara = lineac.split("{")  # Se separa la linea por el caracter {
    if not len(vara) == 2:  # Se comprueba que la longitud de la lista sea 2
        abort()  # Si no se cumple la condición aborta el programa
    else:
        if vara[0].startswith("(") is False or vara[0].startswith("(") is False:
            abort()  # Si no se cumple la condición aborta el programa
        else:
            cond = vara[0].removesuffix(")").removeprefix("(")
            condicion(cond, variables_loc)  # Se ejecuta la función condicion
        if not vara[1].endswith("}"):
            abort()  # Si no se cumple la condición de } aborta el programa
        else:
            coman = vara[1].strip("}").split(";")
            comando(variables_loc, coman)  # Se ejecuta la función comando


# Maneja if en caso de haber un else
def elseDef(linea, variables_loc):  # (else {})
    """ :param linea: 1 línea del archivo .txt :param variables_loc: lista de variables locales """
    vari = linea.split("else")  # Se separa por else
    ifNormal(vari[0], variables_loc)  # Se ejecuta la función ifNormal
    if vari[1].startswith("{") is False or vari[1].endswith("}") is False:
        abort()  # Se comprueba que el else tenga {} si no aborta
    else:
        limp = vari[1].removesuffix("}").removeprefix("{").split(";")  # Se limpia el else y se separa por ;
        comando(variables_loc, limp)  # Se ejecuta la función comando


# Maneja while
def metodo_while(linea, variables_loc):
    """ :param linea: 1 línea del archivo .txt :param variables_loc: lista de variables locales """
    varb = linea.replace(" ", "").removeprefix("while").removesuffix("od")

    if linea.endswith("od") is False or "do" not in varb:  # Se comprueba que termine con od y que se encuentre do
        abort()  # Si no se cumple la condición aborta el programa
    else:
        varn = varb.split("do")[0].removesuffix(")").removeprefix("(")
        condicion(varn, variables_loc)  # Se ejecuta la función condicion
        a = varb.split("do")[1].removesuffix("}").removeprefix("{").split(";")
        comando(variables_loc, a)  # Se ejecuta la función comando


# Maneja repeat
def metodo_repeat(lon, variables_loc):
    """ :param lon: 1 línea del archivo .txt :param variables_loc: lista de variables locales """
    if not lon.endswith("per"):
        abort()
    else:
        perry = lon.removeprefix("repeatTimes").removesuffix("per").split("{")
        if len(perry) < 2:
            abort()
        else:
            if not perry[0].isnumeric():
                isVar(variables_loc, perry[0])
            comando(variables_loc, perry[1].strip("}").split(";"))


"""Condicionales"""


# Maneja las condiciones
def condicion(linea, lista):
    """ :param linea: 1 línea del archivo .txt :param lista: lista de variables locales """
    if "(" in linea and linea.replace(" ", "").endswith(")"):
        p = linea.replace(" ", "").split("(")
        if p[0] == "isfacing":  # Si la condición es isfacing lo envía a la función isfacing
            facing(linea)
        elif p[0] == "isValid":  # Si la condición es isValid lo envía a la función valido
            valido(linea, lista)
        elif p[0] == "canWalk":
            walk(linea, lista)  # Si la condición es canWalk lo envía a la función walk
        elif p[0] == "not":
            if len(linea.split("(")) < 2 or linea.endswith(")") is False:
                abort()  # Si la condición es not y no tiene paréntesis o no tiene ) aborta
            else:
                eso = linea.replace(" ", "").removeprefix("not(").removesuffix(")")
                condicion(eso, lista)  # Si la condición es not y tiene paréntesis se ejecuta la función condicion
        else:
            abort()  # Si no se cumple ninguna condición aborta el programa
    else:
        abort()  # Si no se cumple ninguna condición aborta el programa


# Maneja isfacing
def facing(lin):  # Solo tiene 1 var
    """ :param lin: 1 línea del archivo .txt """
    if "(" in lin and ")" in lin:  # Se comprueba que tenga ( y )
        var = lin.split("(")  # Se separa por (
        par = var[1].strip(")")  # Se quita el )
        if len(var[1].split(",")) > 1:  # Se comprueba que tenga mas de 1 var
            abort()  # Si no se cumple la condición aborta el programa
        else:
            is_orie(par)  # Si se cumple la condición se ejecuta la función is_orie
    else:
        abort()  # Si no se cumple la condición aborta el programa


"""Comandos"""


# Maneja el método Constru
def conStru(j, variables_loc):
    """ :param j: 1 línea del archivo .txt :param variables_loc: lista de variables locales """
    proc = j.replace(" ", "").split("(")  # Se separa por (
    if proc[0] == "if":  # Si el comando es if se ejecuta la función metodo_if
        metodo_if(j.replace(" ", ""), variables_loc)
    elif proc[0] == "while":  # Si el comando es while se ejecuta la función metodo_while
        metodo_while(j.replace(" ", ""), variables_loc)
    elif j.startswith("repeatTimes"):  # Si el comando es repeatTimes se ejecuta la función metodo_repeat
        metodo_repeat(j.replace(" ", ""), variables_loc)


# Maneja el método comando
def comando(variables_loc, stringLista):
    """ :param variables_loc: lista de variables locales :param stringLista: lista de comandos """
    for j in stringLista:
        if "(" in j and ")" in j:
            proc = j.replace(" ", "").split("(")
            if proc[0] == "walk": # Si el comando es walk se ejecuta la función walk
                walk(j, variables_loc)
            elif proc[0] == "jump" or proc[0] == "drop" or proc[0] == "grab" or proc[0] == "get" or proc[0] == "free": # Si el comando es jump, drop, grab, get o free se ejecuta la función caso1
                caso1(j, variables_loc)
            elif proc[0] == "jumpTo":
                caso2(j, variables_loc) # Si el comando es jumpTo se ejecuta la función caso2
            elif proc[0] == "veer" or proc[0] == "look":
                caso3(j)                # Si el comando es veer o look se ejecuta la función caso3
            elif proc[0] == "if" or proc[0] == "while" or j.startswith("repeatTimes"):
                conStru(j, variables_loc) # Si el comando es if, while o repeatTimes se ejecuta la función conStru
            elif proc[0] in dic_PROC.keys():
                dicProc(j.removeprefix(proc[0]), proc[0]) # Si el comando es una función de procesamiento se ejecuta la función dicProc
            else:
                abort() # Si no se cumple ninguna condición aborta el programa
        else:  # revisar si es una asignacion
            asig(j)


def asig(j):
    """ :param j: 1 línea del archivo .txt """
    dummy = False
    for v in variables_globales: # Se comprueba que la variable no esté en variables globales
        if j.split(":")[0] == v: # Si la variable está en variables globales se convierte a dummy=True
            dummy = True
    if dummy is False:          # Si dummy es False aborta
        abort()
    else:
        var1 = j.split(":=")    # De lo contrario se separa por :=
        if len(var1) == 1 or var1[1].isnumeric() is False:
            abort()             # Si no se cumple la condición aborta el programa


def dicProc(lin, nom):
    """ :param lin: 1 línea del archivo .txt :param nom: nombre del comando """
    num = dic_PROC[nom]
    if len(lin.split(",")) != num:  # Se comprueba que tenga el número de variables correcto
        abort()                     # Si no se cumple la condición aborta el programa
    else:
        lini = lin.removeprefix("(").removesuffix(")").replace(" ", "").split(",")  # Se quita los paréntesis y se separa por ,
        for l in lini:
            if not l.isnumeric():   # Se comprueba que todas las variables sean numéricas
                abort()             # Si no se cumple la condición aborta el programa


# definición de walk
def walk(linea, lista):
    """ :param linea: 1 línea del archivo .txt :param lista: lista """
    var = linea.split("(")
    par = var[1].strip(")").replace(" ", "").split(",") # Se quita los paréntesis y se separa por ,
    if len(var[1].split(",")) == 1:
        caso1(linea, lista)                             # Si solo tiene 1 var se ejecuta la función caso1
    elif len(var[1].split(",")) == 2:
        if par[0] not in direcciones:
            if par[0] not in orientaciones:
                abort()                                 # Si la primera var no es una dirección o una orientación aborta el programa
        if not par[1].isnumeric():                      # no es un número se verifica que es variable
            isVar(lista, par[1])                        # Si es variable se ejecuta la función isVar
    elif len(var[1].split(",")) > 2:
        abort()                                         # Si tiene mas de 2 variables aborta el programa

# definición de valido
def valido(linea, lista):
    """ :param linea: 1 línea del archivo .txt :param lista: lista """
    if "(" in linea and ")" in linea:                   # Se comprueba que tenga paréntesis
        var = linea.replace(" ", "").split("(")
        paras = var[1].strip(")").split(",")            # Se separa por ,

        if not len(var[1].split(",")) == 2:             # Se comprueba que tenga 2 variables
            abort()                                     # Si no se cumple la condición aborta el programa
        else:
            if paras[0] not in ins:
                abort()                                 # Si la primera variable no es una instrucción aborta el programa
            elif not paras[1].isnumeric():              # no es un número se verifica que es variable (nombre o variable)
                isVar(lista, paras[1])                  # Si es variable se ejecuta la función isVar
    else:
        abort()                                         # Si no tiene paréntesis aborta el programa

# Definición del bloque de PROC
def proc(bloque):
    """ :param bloque:bloque del archivo .txt """
    variables_loc = primeralproc(bloque[0])             # Se analiza la primera línea de PROC
    bloque.pop(0)
    bloque.pop(-1)                                      # Se eliminan PROC y CORP
    string_bloque = ""
    for i in bloque:
        string_bloque += i                              # Se concatena cada línea del bloque
    sb = string_bloque.replace(" ", "").replace("\n", "")
    if sb.startswith("{") is False or sb.endswith("}") is False: # Se comprueba que el bloque empiece y termine con { y }
        abort()                                                  # Si no se cumple la condición aborta el programa
    stringLista = sb.strip("{}").split(";")
    comando(variables_loc, stringLista)                 # Se ejecuta la función comando

# Definición del bloque final
def bloque(bloq):
    """ :param bloq:bloque del archivo .txt """
    string_bloque = ""
    for i in bloq:
        string_bloque += i                            # Se concatena cada línea del bloque
    sb = string_bloque.replace(" ", "").replace("\n", "")  # Se quita los espacios y los saltos de línea
    if sb.startswith("{") is False or sb.endswith("}") is False:
        abort()                                       # Si no se cumple la condición aborta el programa
    else:
        stringLista = sb.strip("{}").split(";")       # Se separa por ; y se borran {}
        if sb.count(";") != len(stringLista) - 1:     # Se comprueba que haya tantos ; como líneas
            abort()                                   # Si no se cumple la condición aborta el programa
        else:
            comando(None, stringLista)                # Se ejecuta la función comando


# verifica si es una variable del programa
def var(linea):
    """ :param linea: 1 línea del archivo .txt """
    leni = linea.replace(" ", "").replace("\n", "").removeprefix("VAR")
    if leni.endswith(";") is False:  # si el ultimo caracter no es un punto y coma
        abort()  # aborta
    else:
        varia = leni.removesuffix(";").split(",")  # se separa la linea por comas
        if leni.count(",") != len(varia) - 1:  # si hay mas comas que variables
            abort()  # aborta
        else:
            alphaNum(varia)  # busca si es alfanumérico de lo contrario
    return varia


# Se encarga de verificar si es alfanumérico
def alphaNum(lista):
    """ :param lista: lista """
    for f in lista:
        if f.isalnum() is False or f[0].isalpha() is False: # si no es alfanumérico o no es una letra
            abort()                                         # aborta


##############################################
"""PROGRAMA PRINCIPAL"""
##############################################

with open("prueba.txt", 'r') as f:  # se abre el archivo con el nombre texto.txt
    lines = f.readlines()  # se lee el archivo y se guarda en una lista

string_bloque1 = ""
for i in lines:
    string_bloque1 += i                           # Se concatena cada línea del archivo
string_bloque = string_bloque1.replace(" ", "").replace("\n", "") # Se quita los espacios y los saltos de línea

if string_bloque.count("{") % 2 == 0 or string_bloque.count("}") % 2 == 0 or string_bloque.count("(") % 2 == 0 or string_bloque.count(")") % 2 == 0:
    # Revisa primera linea de programa
    if string_bloque.startswith("PROG") and string_bloque.endswith("GORP"):  # si la primera linea no es PROG se termina el programa
        i = 1
        while i < len(lines[1:-1]):  # Se salta la primera linea y última linea del archivo
            """PARTE A: VAR"""
            l = lines[i].replace("\n", "").replace(" ", "")
            if not l == "":  # si la linea no es un espacio se revisa si es una declaración de variables
                if l.startswith("VAR"):  # si la linea inicia con VAR se revisa si es una declaración de variables
                    variables_globales.extend(var(l))  # se guardan las variables en una lista
                elif l.startswith("PROC"): # si la linea inicia con PROC se revisa si es una declaración de PROC
                    indexProc = i      # se guarda el índice de la línea de PROC
                    indexCorp = -1     # se guarda el índice de CORP
                    dummy = False
                    j = indexProc + 1 # se actualiza el índice de la línea
                    while j < len(lines[1:-1]) and dummy is False:
                        t = lines[j].replace("\n", "").replace(" ", "")
                        if t.startswith("PROC"): # si la línea inicia con PROC
                            break                # se termina el ciclo
                        elif t.startswith("CORP"):
                            dummy = True         # se actualiza el índice de CORP
                            indexCorp = j
                        j += 1
                    if dummy:
                        proc(lines[indexProc:indexCorp + 1])
                    else:
                        abort()
                    i = indexCorp
                elif l.startswith("{"):
                    indexcorchi = i    # se guarda el índice de la línea de { del corchete de inicio
                    indexcorchf = -1   # se guarda el índice de la línea de } del corchete de fin
                    dummy = False
                    j = indexcorchi + 1
                    while j < len(lines[1:-1]) and dummy is False: # meintras que el índice de la línea no sea mayor que el tamaño de la lista y el dummy sea falso
                        t = lines[j].replace("\n", "").replace(" ", "") # se quita los espacios y los saltos de línea
                        if t.startswith("{"):                # si la línea inicia con {
                            break                           # se termina el ciclo
                        elif t.startswith("}"):            # si la línea inicia con }
                            dummy = True                  # se actualiza el índice de }
                            indexcorchf = j
                        j += 1
                    if dummy:
                        bloque(lines[indexcorchi:indexcorchf + 1]) # se ejecuta la función bloque
                    else:
                        abort()                                   # si no se cumple la condición aborta el programa
                    i = indexcorchf
                else:
                    abort()                                      # si no se cumple la condición aborta el programa
            i += 1                                               # se actualiza el índice de la línea
    else:
        abort()                                                  # si no se cumple la condición aborta el programa
else:
    abort()                                                      # si no se cumple la condición aborta el programa

print("SI")                                                      # Si el programa está bien escrito imprime SI
