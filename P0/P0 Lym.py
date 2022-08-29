"""Notas Proyecto 0"""
# P0 Lym

# M: to move forward
# R: to turn right
# C: to drop a chip
# B: to place a balloon
# c: to pickup a chip
# b: to grab a balloon
# P: to pop a balloon
# J(n): to jump forward n steps. It may jump over obstacles, but the final postion sould not have an obstacle.
# G(x,y): to go to position (x,y). Position (x,y) should not have an obstacle.
# class uniandes.lym.robot.kernel. RootWorldDec


# A program defintion begins with the keyword PROG
# It ends the keyword GORP
# A declaration of variables is the keyword VAR followed by a list of names separated by commas.
# A name is a string of alphanumeric characters that begins with a letter
# The list is followed by ;
# A procedure defintion is a the word PROC followed by a name followed by a list of parameters within parenthesis separated by commas,
#  followed by a block of instructions and ending with the word CORP.
# A block of instructions is a sequence of instructions separated by semicolons within curly brackets.
# An instruction can be a command,a control structure or a procedure call.
# Spaces, newlines, and tabulators are separators and should be ignored.

# Command:
# An assignment: name := n where name is a variable name and n is a number. The result of this instruction is to assign the value of the number to the variable.
# walk(n) – where n is a number or a variable or a parameter. The robot should move n steps forward.
# jump(n) – where n is a number or a variable or a parameter. The robot should jump n steps forward.
# jumpTo(n,m) – where n and m are numbers, variables, or parameters. The robot should jump to position (n,m).
# veer(D) – where D can be left, right, or around. The robot should turn 90 degrees in the direction D.
# look(O) – where O can be north, south, east or west. The robot should turn so that it ends up facing direction O.
# drop(n) – where n is a number or a variable or a parameter. The Robot should put n chips from its position.
# grab(n) – where n is a number or a variable or a parameter. The Robot should get n ballons from its position.
# get(n) – where n is a number or a variable or a parameter. The Robot should get n chips from its position.
# free(n) – where n is a number or a variable or a parameter. The Robot should put n balloons from its position.
# pop(n) – where n is a number or a variable or a parameter. The Robot should pop n balloons from its position.
# walk(d,n) – where n is a number or a variable or a parameter; d is a direction, either front, right, left, back. The robot should move n positions to the front, to the left, the right or back and end up facing the same direction as it started.
# walk(o,n) – where n is a number or a variable or a parameter; o is north, south, west, or east. The robot should face O and then move n steps.

# Control Structure:
#     Conditional: if (condition)Block1 else Block2 fi – Executes Block1 if condition is true and Block2 if condition is false.
#     Conditional if (condition)Block1 fi– Executes Block1 if condition is true does not do anything if it is false.
#     Loop: while (condition)do Block od – Executes Block while condition is true.
#     Repeat: repeatTimes n Block per – Executes Block n times, where n is a variable or a parameter or a number.

# Conditions:
# isfacing(O) – where O is one of: north, south, east, or west
# isValid(ins,n) – where ins can be walk, jump, grab, pop, pick, free, drop and n is a number or a variable. It is true if ins(n) can be executed without error.
# canWalk(d,n) – where D is one of: north, south, east, or west and n is a number, a variable or a parameter.
# canWalk(o,n) – where D is one of: right, left, front, or back and n is a number, a variable or a parameter.
# not (cond) – where cond is a condition

# Implement a simple yes/no parser. Verify whether the syntax is correct. You must verify that used function names
# and variable names have been previously defined or in the case of functions, that they are the function’s
# arguments. allow recursion


"""PROGRAMA"""

import sys  # se importa sys para poder usar sys.exit()

"""Definición de parámetros GLOBALES"""

variables_globales = []  # se generan variables globales para poder usarlas en todo el programa
dic_PROC = {}
direcciones = ["left", "right", "around"]
orientaciones = ["north", "south", "east", "west"]
ins = ["walk", "jump", "grab", "pop", "pick", "free", "drop"]
comandos = ["walk", "jump", "jumpTo", "veer", "look", "drop", "grab", "get", "free", "pop"]


"""Definición de CASOS"""
#LISTOOO
def caso1(linea, variables):  # n
    var = linea.split("(")  # Se separa la linea por el caracter (
    par = var[1].strip(")")  # Se quita el caracter ) de la linea
    if len(var[1].split(",")) > 1:  # Si la longitud de la lista es mayor a 1
        abort()
    elif par.isnumeric() is False:  # no es un número se verifica que es variable o parámetro
        isVar(variables, par)  # Si no aborta el proceso continúa

#LSITOOO
def caso2(linea, lista):
    var = linea.split("(")
    # jump(a,b) var=["jump",["a","b"]]
    paras = var[1].strip(")").replace(" ","").split(",")
    if not len(var[1].split(",")) == 2:
        abort()
    else:
        for p in paras:
            if p.isnumeric() is False: 
                isVar(lista, p)

#Perfectoo
def caso3(linea):
    var = linea.split("(")
    par = var[1].strip(")")
    if not len(var[1].split(",")) ==1:
        abort()
    elif par.isnumeric():
        abort()
    elif var[0] == "veer":
        is_dir(par)
    elif var[0] == "look":
        is_orie(par)
#YAAA
def is_orie(linea):
    if linea not in orientaciones:
        abort()
#YAAAA
def is_dir(linea):
    if linea not in direcciones:
        abort()

#listo
def isVar(lista, var):
    if lista is not None:
        if var not in lista:
            if var not in variables_globales:
                abort()
    else:
        if var not in variables_globales:
                abort()


"""DEFINICIONES SECUNDARIAS"""

#bebe ya
def abort():  # se aborta el programa
    print("NO")
    sys.exit()

#funcionaa
def primeralproc(linea1):
    linea=linea1.replace("\n","")
    variables_locales = []
    proc = linea.replace(" ", "").replace("\n","").removeprefix("PROC").split("(")   # lista separada PROC y resto de (nota!!!!!!: CASO PROC CB)
    if len(proc) == 1 or linea.endswith(")") is False or len(proc[1].removesuffix(")").split(",")) - 1 != proc[1].count(",") or len(proc[0])==0:  # Se comprueba que los prámetros se encuentren dentro del paréntesis
        abort()
    else:
        dic_PROC[proc[0]] = len(proc[1].split(","))  # se extrae el nombre de la función y se mete por si se utiliza luego
        if len(proc[1].split(",")) >1:
            for x in proc[1].removesuffix(")").split(","):  # NOTA!!!: Hace falta revisar el caso de las comas (,)
                if x.isalnum() and x[0].isalpha():
                    variables_locales.append(x)
                else:
                    abort()

    return variables_locales


"""Estructuras de control"""


#YAAAA
# Maneja condicionales de if
def metodo_if(linea, variables_loc):
    lineac = linea.removeprefix("if").removesuffix("fi")
    if not linea.endswith("fi"):
        abort()
    elif "else" in lineac:
        elseDef(lineac, variables_loc)
    else:
        ifNormal(lineac, variables_loc)

#YAAA
# Maneja if sencillo (una condicion y un bloque)
def ifNormal(lineac, variables_loc):
    vara = lineac.split("{")
    if not len(vara) == 2:
        abort()
    else:
        if vara[0].startswith("(") is False or vara[0].startswith("(") is False:
            abort()
        else:
            cond = vara[0].removesuffix(")").removeprefix("(")
            condicion(cond, variables_loc)
        if not vara[1].endswith("}"):
            abort()
        else:
            coman = vara[1].strip("}").split(";")
            comando(variables_loc, coman)

#YAAAAA
# Maneja if en caso de haber un else
def elseDef(linea, variables_loc):  # (else {})
    vari = linea.split("else")
    ifNormal(vari[0], variables_loc)
    if vari[1].startswith("{") is False or vari[1].endswith("}") is False:
        abort()
    else:
        limp = vari[1].removesuffix("}").removeprefix("{").split(";")
        comando(variables_loc, limp)

#YAAA
# Maneja while
def metodo_while(linea, variables_loc):
    varb = linea.replace(" ", "").removeprefix("while").removesuffix("od")
    # while ( canWalk ( north ,1) ) do { walk ( north ,1) } od
    # [( canWalk ( north ,1) ), walk ( north ,1)]
    if linea.endswith("od") is False or "do" not in varb:
        abort()
    else:
        varn = varb.split("do")[0].removesuffix(")").removeprefix("(")
        condicion(varn, variables_loc)
        a=varb.split("do")[1].removesuffix("}").removeprefix("{").split(";")
        comando(variables_loc, a)

#YAAAAA
# Maneja repeat
def metodo_repeat(lon, variables_loc):
    if not lon.endswith("per"):
        abort()
    else:
        perry = lon.removeprefix("repeatTimes").removesuffix("per").split("{")
        if len(perry) < 2:
            abort()
        else:
            if not perry[0].isnumeric():
                isVar( variables_loc, perry[0])
            comando(variables_loc, perry[1].strip("}").split(";"))


"""Condicionales"""


#listo
def condicion(linea, lista):
    if "(" in linea and linea.replace(" ","").endswith(")"):
        p=linea.replace(" ","").split("(")
        if p[0]=="isfacing":
            facing(linea)
        elif p[0]=="isValid":
            valido(linea, lista)
        elif p[0]=="canWalk":
            walk(linea, lista)
        elif p[0]=="not":
            if len(linea.split("(")) < 2 or linea.endswith(")") is False:
                abort()
            else:
                eso = linea.replace(" ","").removeprefix("not(").removesuffix(")")
                condicion(eso, lista)
        else: abort()
    else: abort()


#listoooo
def facing(lin):  # Solo tiene 1 var
    if "(" in lin and ")" in lin:
        var = lin.split("(")
        par = var[1].strip(")")
        if len(var[1].split(",")) > 1:
            abort()
        else:
            is_orie(par)
    else:
        abort()


"""Comandos"""

#YAAAA
def conStru(j ,variables_loc):
    proc = j.replace(" ","").split("(")
    if proc[0]=="if":
        metodo_if(j.replace(" ",""), variables_loc)
    elif proc[0]=="while":
        metodo_while(j.replace(" ",""), variables_loc)
    elif j.startswith("repeatTimes"):
        metodo_repeat(j.replace(" ",""), variables_loc)

#PERFECTOOO
def comando(variables_loc, stringLista):
    for j in stringLista:
        if "(" in j and ")" in j:
            proc = j.replace(" ","").split("(")
            if proc[0]=="walk":
                walk(j, variables_loc)
            elif proc[0]=="jump" or proc[0]=="drop" or proc[0]=="grab" or proc[0]=="get" or proc[0]=="free":
                caso1(j, variables_loc)
            elif proc[0]=="jumpTo":
                caso2(j, variables_loc)
            elif proc[0]=="veer" or proc[0]=="look":
                caso3(j)
            elif proc[0]=="if" or proc[0]=="while" or j.startswith("repeatTimes"):
                conStru(j, variables_loc)
            elif proc[0] in dic_PROC.keys():
                dicProc(j.removeprefix(proc[0]), proc[0])
            else:
                abort()
        else: # revisar si es una asignacion
            asig(j)

#bieeen         
def asig(j):
    dummy = False
    for v in variables_globales:
        if j.split(":")[0]==v:
            dummy = True
    if dummy is False:
        abort()
    else:
        var1 = j.split(":=")
        if len(var1) == 1 or var1[1].isnumeric() is False:
            abort()

#LISTO
def dicProc(lin, nom):
    num = dic_PROC[nom]
    if len(lin.split(",")) != num:
        abort()
    else:
        lini = lin.removeprefix("(").removesuffix(")").replace(" ","").split(",")
        for l in lini:
            if not l.isnumeric():
                abort()

#preparado
def walk(linea, lista):
    var = linea.split("(")
    par = var[1].strip(")").replace(" ","").split(",")
    if len(var[1].split(",")) == 1:
        caso1(linea, lista)
    elif len(var[1].split(",")) == 2:
        # ["walk",["d/o",n"]]
        if par[0] not in direcciones:
            if par[0] not in orientaciones:
                abort()
        if not par[1].isnumeric():  # no es un número se verifica que es variable
            isVar(lista, par[1])
    elif len(var[1].split(",")) > 2:
        abort()

#DURO PERO YA
def valido(linea, lista):
    if "(" in linea and ")" in linea:
        var = linea.replace(" ","").split("(")
        paras = var[1].strip(")").split(",")

        if not len(var[1].split(",")) == 2:
            abort()
        else:
            if paras[0] not in ins:
                abort()
            elif not paras[1].isnumeric():  # no es un número se verifica que es variable (nombre o variable)
                isVar(lista, paras[1])
    else:
        abort()

#TERMINADAAAA
def proc(bloque):
    variables_loc = primeralproc(bloque[0])
    bloque.pop(0)
    bloque.pop(-1)
    string_bloque = ""
    for i in bloque:
        string_bloque += i
    sb=string_bloque.replace(" ", "").replace("\n","")
    if sb.startswith("{") is False or sb.endswith("}") is False:
        abort()
    stringLista = sb.strip("{}").split(";")
    comando(variables_loc, stringLista)

#hermoso
def bloque(bloq):
    string_bloque = ""
    for i in bloq:
        string_bloque += i
    sb=string_bloque.replace(" ", "").replace("\n","")
    if sb.startswith("{") is False or sb.endswith("}") is False:
        abort()
    else:
        stringLista = sb.strip("{}").split(";")
        if sb.count(";") != len(stringLista) - 1:
            abort()
        else:
            comando(None, stringLista)

            # [go(3,3)],[n=6],[putCB (2 ,1)]

#ES PERFECTOOOOO
# ENTRA UN STRING
def var(linea):
    leni = linea.replace(" ", "").replace("\n","").removeprefix("VAR")
    # n, x, y; # se elimina el comando VAR
    if leni.endswith(";") is False:  # si el ultimo caracter no es un punto y coma
        abort()
    else:
        varia = leni.removesuffix(";").split(",")  # se separa la linea por comas
        if leni.count(",") != len(varia) - 1:  # si hay mas comas que variables
            abort()
        else:
            alphaNum(varia)
    return varia

#FUNCIONAAA
# revisa q sea alfanumerico
def alphaNum(lista):
    for f in lista:
        if f.isalnum() is False or f[0].isalpha() is False:
            abort()


##############################################
"""PROGRAMA PRINCIPAL"""
##############################################

with open("prueba.txt", 'r') as f:  # se abre el archivo con el nombre texto.txt
    lines = f.readlines()  # se lee el archivo y se guarda en una lista

string_bloque1 = ""
for i in lines:
    string_bloque1 += i
string_bloque=string_bloque1.replace(" ", "").replace("\n","")

if string_bloque.count("{") % 2 == 0 or string_bloque.count("}") % 2 == 0 or string_bloque.count( "(") % 2 == 0 or string_bloque.count(")") % 2 == 0:
    # Revisa primera linea de programa
    if string_bloque.startswith("PROG") and string_bloque.endswith("GORP"):  # si la primera linea no es PROG se termina el programa
        i = 1
        while i < len(lines[1:-1]):  # Se salta la primera linea y última linea del archivo
            """PARTE A: VAR"""
            l = lines[i].replace("\n","").replace(" ","")
            if not l =="":  # si la linea no es un espacio se revisa si es una declaración de variables
                if l.startswith("VAR"):  # si la linea inicia con VAR se revisa si es una declaración de variables
                    variables_globales.extend(var(l))  # se guardan las variables en una lista
                elif l.startswith("PROC"):
                    indexProc = i
                    indexCorp = -1
                    dummy = False
                    j=indexProc + 1
                    while(j<len(lines[1:-1]) and dummy is False):
                        t=lines[j].replace("\n","").replace(" ","")
                        if t.startswith("PROC"):
                            break
                        elif t.startswith("CORP"):
                            dummy = True
                            indexCorp = j
                        j += 1
                    if dummy:
                        proc(lines[indexProc:indexCorp + 1])
                    else:
                        abort()
                    i = indexCorp
                elif l.startswith("{"):
                    indexcorchi = i########
                    indexcorchf = -1
                    dummy = False
                    j=indexcorchi + 1
                    while(j<len(lines[1:-1]) and dummy is False):
                        t=lines[j].replace("\n","").replace(" ","")
                        if t.startswith("{"):
                            break
                        elif t.startswith("}"):
                            dummy = True
                            indexcorchf = j
                        j += 1
                    if dummy:
                        bloque(lines[indexcorchi:indexcorchf + 1])
                    else:
                        abort()
                    i = indexcorchf
                else:
                    abort()
            i += 1
    else:
        abort()
else: abort()

print("SI")


#%%

"""PROGRAMA"""

import sys  # se importa sys para poder usar sys.exit()

"""Definición de parámetros GLOBALES"""

variables_globales = []  # se generan variables globales para poder usarlas en todo el programa
dic_PROC = {}
direcciones = ["left", "right", "around"]
orientaciones = ["north", "south", "east", "west"]
ins = ["walk", "jump", "grab", "pop", "pick", "free", "drop"]
comandos = ["walk", "jump", "jumpTo", "veer", "look", "drop", "grab", "get", "free", "pop"]


"""Definición de CASOS"""
#LISTOOO
def caso1(linea, variables):  # n
    var = linea.split("(")  # Se separa la linea por el caracter (
    par = var[1].strip(")")  # Se quita el caracter ) de la linea
    if len(var[1].split(",")) > 1:  # Si la longitud de la lista es mayor a 1
        abort()
    elif par.isnumeric() is False:  # no es un número se verifica que es variable o parámetro
        isVar(variables, par)  # Si no aborta el proceso continúa

#LSITOOO
def caso2(linea, lista):
    var = linea.split("(")
    # jump(a,b) var=["jump",["a","b"]]
    paras = var[1].strip(")").replace(" ","").split(",")
    if not len(var[1].split(",")) == 2:
        abort()
    else:
        for p in paras:
            if p.isnumeric() is False: 
                isVar(lista, p)

#Perfectoo
def caso3(linea):
    var = linea.split("(")
    par = var[1].strip(")")
    if not len(var[1].split(",")) ==1:
        abort()
    elif par.isnumeric():
        abort()
    elif var[0] == "veer":
        is_dir(par)
    elif var[0] == "look":
        is_orie(par)
#YAAA
def is_orie(linea):
    if linea not in orientaciones:
        abort()
#YAAAA
def is_dir(linea):
    if linea not in direcciones:
        abort()

#listo
def isVar(lista, var):
    if lista is not None:
        if var not in lista:
            if var not in variables_globales:
                abort()
    else:
        if var not in variables_globales:
                abort()


"""DEFINICIONES SECUNDARIAS"""

#bebe ya
def abort():  # se aborta el programa
    print("NO")
    sys.exit()

#funcionaa
def primeralproc(linea1):
    linea=linea1.replace("\n","")
    variables_locales = []
    proc = linea.replace(" ", "").replace("\n","").removeprefix("PROC").split("(")   # lista separada PROC y resto de (nota!!!!!!: CASO PROC CB)
    if len(proc) == 1 or linea.endswith(")") is False or len(proc[1].removesuffix(")").split(",")) - 1 != proc[1].count(",") or len(proc[0])==0:  # Se comprueba que los prámetros se encuentren dentro del paréntesis
        abort()
    else:
        dic_PROC[proc[0]] = len(proc[1].split(","))  # se extrae el nombre de la función y se mete por si se utiliza luego
        if len(proc[1].split(",")) >1:
            for x in proc[1].removesuffix(")").split(","):  # NOTA!!!: Hace falta revisar el caso de las comas (,)
                if x.isalnum() and x[0].isalpha():
                    variables_locales.append(x)
                else:
                    abort()

    return variables_locales


"""Estructuras de control"""


#YAAAA
# Maneja condicionales de if
def metodo_if(linea, variables_loc):
    lineac = linea.removeprefix("if").removesuffix("fi")
    if not linea.endswith("fi"):
        abort()
    elif "else" in lineac:
        elseDef(lineac, variables_loc)
    else:
        ifNormal(lineac, variables_loc)

#YAAA
# Maneja if sencillo (una condicion y un bloque)
def ifNormal(lineac, variables_loc):
    vara = lineac.split("{")
    if not len(vara) == 2:
        abort()
    else:
        if vara[0].startswith("(") is False or vara[0].startswith("(") is False:
            abort()
        else:
            cond = vara[0].removesuffix(")").removeprefix("(")
            condicion(cond, variables_loc)
        if not vara[1].endswith("}"):
            abort()
        else:
            coman = vara[1].strip("}").split(";")
            comando(variables_loc, coman)

#YAAAAA
# Maneja if en caso de haber un else
def elseDef(linea, variables_loc):  # (else {})
    vari = linea.split("else")
    ifNormal(vari[0], variables_loc)
    if vari[1].startswith("{") is False or vari[1].endswith("}") is False:
        abort()
    else:
        limp = vari[1].removesuffix("}").removeprefix("{").split(";")
        comando(variables_loc, limp)

#YAAA
# Maneja while
def metodo_while(linea, variables_loc):
    varb = linea.replace(" ", "").removeprefix("while").removesuffix("od")
    # while ( canWalk ( north ,1) ) do { walk ( north ,1) } od
    # [( canWalk ( north ,1) ), walk ( north ,1)]
    if linea.endswith("od") is False or "do" not in varb:
        abort()
    else:
        varn = varb.split("do")[0].removesuffix(")").removeprefix("(")
        condicion(varn, variables_loc)
        a=varb.split("do")[1].removesuffix("}").removeprefix("{").split(";")
        comando(variables_loc, a)

#YAAAAA
# Maneja repeat
def metodo_repeat(lon, variables_loc):
    if not lon.endswith("per"):
        abort()
    else:
        perry = lon.removeprefix("repeatTimes").removesuffix("per").split("{")
        if len(perry) < 2:
            abort()
        else:
            if not perry[0].isnumeric():
                isVar( variables_loc, perry[0])
            comando(variables_loc, perry[1].strip("}").split(";"))


"""Condicionales"""


#listo
def condicion(linea, lista):
    if "(" in linea and linea.replace(" ","").endswith(")"):
        p=linea.replace(" ","").split("(")
        if p[0]=="isfacing":
            facing(linea)
        elif p[0]=="isValid":
            valido(linea, lista)
        elif p[0]=="canWalk":
            walk(linea, lista)
        elif p[0]=="not":
            if len(linea.split("(")) < 2 or linea.endswith(")") is False:
                abort()
            else:
                eso = linea.replace(" ","").removeprefix("not(").removesuffix(")")
                condicion(eso, lista)
        else: abort()
    else: abort()


#listoooo
def facing(lin):  # Solo tiene 1 var
    if "(" in lin and ")" in lin:
        var = lin.split("(")
        par = var[1].strip(")")
        if len(var[1].split(",")) > 1:
            abort()
        else:
            is_orie(par)
    else:
        abort()


"""Comandos"""

#YAAAA
def conStru(j ,variables_loc):
    proc = j.replace(" ","").split("(")
    if proc[0]=="if":
        metodo_if(j.replace(" ",""), variables_loc)
    elif proc[0]=="while":
        metodo_while(j.replace(" ",""), variables_loc)
    elif j.startswith("repeatTimes"):
        metodo_repeat(j.replace(" ",""), variables_loc)

#PERFECTOOO
def comando(variables_loc, stringLista):
    for j in stringLista:
        if "(" in j and ")" in j:
            proc = j.replace(" ","").split("(")
            if proc[0]=="walk":
                walk(j, variables_loc)
            elif proc[0]=="jump" or proc[0]=="drop" or proc[0]=="grab" or proc[0]=="get" or proc[0]=="free":
                caso1(j, variables_loc)
            elif proc[0]=="jumpTo":
                caso2(j, variables_loc)
            elif proc[0]=="veer" or proc[0]=="look":
                caso3(j)
            elif proc[0]=="if" or proc[0]=="while" or j.startswith("repeatTimes"):
                conStru(j, variables_loc)
            elif proc[0] in dic_PROC.keys():
                dicProc(j.removeprefix(proc[0]), proc[0])
            else:
                abort()
        else: # revisar si es una asignacion
            asig(j)

#bieeen         
def asig(j):
    dummy = False
    for v in variables_globales:
        if j.split(":")[0]==v:
            dummy = True
    if dummy is False:
        abort()
    else:
        var1 = j.split(":=")
        if len(var1) == 1 or var1[1].isnumeric() is False:
            abort()

#LISTO
def dicProc(lin, nom):
    num = dic_PROC[nom]
    if len(lin.split(",")) != num:
        abort()
    else:
        lini = lin.removeprefix("(").removesuffix(")").replace(" ","").split(",")
        for l in lini:
            if not l.isnumeric():
                abort()

#preparado
def walk(linea, lista):
    var = linea.split("(")
    par = var[1].strip(")").replace(" ","").split(",")
    if len(var[1].split(",")) == 1:
        caso1(linea, lista)
    elif len(var[1].split(",")) == 2:
        # ["walk",["d/o",n"]]
        if par[0] not in direcciones:
            if par[0] not in orientaciones:
                abort()
        if not par[1].isnumeric():  # no es un número se verifica que es variable
            isVar(lista, par[1])
    elif len(var[1].split(",")) > 2:
        abort()

#DURO PERO YA
def valido(linea, lista):
    if "(" in linea and ")" in linea:
        var = linea.replace(" ","").split("(")
        paras = var[1].strip(")").split(",")

        if not len(var[1].split(",")) == 2:
            abort()
        else:
            if paras[0] not in ins:
                abort()
            elif not paras[1].isnumeric():  # no es un número se verifica que es variable (nombre o variable)
                isVar(lista, paras[1])
    else:
        abort()

#TERMINADAAAA
def proc(bloque):
    variables_loc = primeralproc(bloque[0])
    bloque.pop(0)
    bloque.pop(-1)
    string_bloque = ""
    for i in bloque:
        string_bloque += i
    sb=string_bloque.replace(" ", "").replace("\n","")
    if sb.startswith("{") is False or sb.endswith("}") is False:
        abort()
    stringLista = sb.strip("{}").split(";")
    comando(variables_loc, stringLista)

#hermoso
def bloque(bloq):
    string_bloque = ""
    for i in bloq:
        string_bloque += i
    sb=string_bloque.replace(" ", "").replace("\n","")
    if sb.startswith("{") is False or sb.endswith("}") is False:
        abort()
    else:
        stringLista = sb.strip("{}").split(";")
        if sb.count(";") != len(stringLista) - 1:
            abort()
        else:
            comando(None, stringLista)

            # [go(3,3)],[n=6],[putCB (2 ,1)]

#ES PERFECTOOOOO
# ENTRA UN STRING
def var(linea):
    leni = linea.replace(" ", "").replace("\n","").removeprefix("VAR")
    # n, x, y; # se elimina el comando VAR
    if leni.endswith(";") is False:  # si el ultimo caracter no es un punto y coma
        abort()
    else:
        varia = leni.removesuffix(";").split(",")  # se separa la linea por comas
        if leni.count(",") != len(varia) - 1:  # si hay mas comas que variables
            abort()
        else:
            alphaNum(varia)
    return varia

#FUNCIONAAA
# revisa q sea alfanumerico
def alphaNum(lista):
    for f in lista:
        if f.isalnum() is False or f[0].isalpha() is False:
            abort()


##############################################
"""PROGRAMA PRINCIPAL"""
##############################################

with open("P0/prueba.txt", 'r') as f:  # se abre el archivo con el nombre texto.txt
    lines = f.readlines()  # se lee el archivo y se guarda en una lista

string_bloque1 = ""
for i in lines:
    string_bloque1 += i
string_bloque=string_bloque1.replace(" ", "").replace("\n","")

if string_bloque.count("{") % 2 == 0 or string_bloque.count("}") % 2 == 0 or string_bloque.count( "(") % 2 == 0 or string_bloque.count(")") % 2 == 0:
    # Revisa primera linea de programa
    if string_bloque.startswith("PROG") and string_bloque.endswith("GORP"):  # si la primera linea no es PROG se termina el programa
        i = 1
        while i < len(lines[1:-1]):  # Se salta la primera linea y última linea del archivo
            """PARTE A: VAR"""
            l = lines[i].replace("\n","").replace(" ","")
            if not l =="":  # si la linea no es un espacio se revisa si es una declaración de variables
                if l.startswith("VAR"):  # si la linea inicia con VAR se revisa si es una declaración de variables
                    variables_globales.extend(var(l))  # se guardan las variables en una lista
                elif l.startswith("PROC"):
                    indexProc = i
                    indexCorp = -1
                    dummy = False
                    j=indexProc + 1
                    while(j<len(lines[1:-1]) and dummy is False):
                        t=lines[j].replace("\n","").replace(" ","")
                        if t.startswith("PROC"):
                            break
                        elif t.startswith("CORP"):
                            dummy = True
                            indexCorp = j
                        j += 1
                    if dummy:
                        proc(lines[indexProc:indexCorp + 1])
                    else:
                        abort()
                    i = indexCorp
                elif l.startswith("{"):
                    indexcorchi = i########
                    indexcorchf = -1
                    dummy = False
                    j=indexcorchi + 1
                    while(j<len(lines[1:-1]) and dummy is False):
                        t=lines[j].replace("\n","").replace(" ","")
                        if t.startswith("{"):
                            break
                        elif t.startswith("}"):
                            dummy = True
                            indexcorchf = j
                        j += 1
                    if dummy:
                        bloque(lines[indexcorchi:indexcorchf + 1])
                    else:
                        abort()
                    i = indexcorchf
                else:
                    abort()
            i += 1
    else:
        abort()
else: abort()

print("SI")


# %%
