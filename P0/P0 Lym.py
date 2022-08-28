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

# Implement a simple yes/no parser.
# Verify whether the syntax is correct.
# You must verify that used function names and variable names have been previously defined or in the case of functions, that they are the function’s arguments.
# allow recursion

"""PROGRAMA"""

from ast import Break
from asyncio.windows_events import NULL
from curses.ascii import isalnum
from pickle import FALSE
import sys  # se importa sys para poder usar sys.exit()

variables_globales = []  # se generan variables globales para poder usarlas en todo el programa
dic_PROC = {}
direcciones = ["left", "right", "around"]
orientaciones = ["north", "south", "east", "west"]
ins = ["walk", "jump", "grab", "pop", "pick", "free", "drop"]
comandos =["walk","jump", "jumpTo","veer", "look", "drop", "grab", "get","free", "pop"]

def abort():
    print("NO")
    sys.exit()

def caso1(linea, variables):  # n
    var = linea.split("(")
    par = var[1].strip(")")
    if len(var[1].split(",")) > 1:
        abort()
    elif par.isnumeric() == False:  # no es un número se verifica que es variable
        isVar(variables, par)  # Si no aborta el proceso continúa


def caso2(linea, lista):
    var = linea.split("(")
    # jump(a,b) var=["jump",["a","b"]]
    paras = var[1].strip(")").split(",")
    if len(var[1].split(",")) > 2:
        abort()
    else:
        for p in paras:
            isVar(lista, p)


def caso3(linea):
    var = linea.split("(")
    par = var[1].strip(")")
    if len(var[1].split(",")) > 1:
        abort()
    elif par.isnumeric():
        abort()
    elif var[0] == "veer":
        is_dir(par)
    elif var[0] == "look":
        is_orie(par)


def is_dir(linea):
    if linea in direcciones == False:
        abort()


def is_orie(linea):
    if linea in orientaciones == False:
        abort()


def isVar(lista, var):
    if lista != None:
        if var in lista == False:
            if var in variables_globales == False:
                abort()


"""DEFINICIONES SECUNDARIAS"""


def primeralproc(linea):
    variables_locales = []
    proc = linea.replace(" ", "").remove("PROC").split("(")  # lista separada PROC y resto de (nota!!!!!!: CASO PROC CB)

    if len(proc) == 1 or linea.endswith(
            ")") == False:  # Se comprueba que los prámetros se encuentren dentro del paréntesis
        abort()
    dic_PROC[proc(0)] = len(proc(1).split(","))  # se extrae el nombre de la función y se mete por si se utiliza luego

    if len(proc(1).remove(")").split(",")) - 1 != proc.count(","):
        abort()

    for x in proc(1).remove(")").split(","):  # NOTA!!!: Hace falta revisar el caso de las comas (,)
        variables_locales.append(x)
    return variables_locales


"""
    indexProc, indexCorp = lines.index(l), lines.index(l)  # se obtiene el indice de la linea PROC
    # se continua con el programa hasta encontrar una linea que inicie con CORP while
    proc(l)
    while lines[indexCorp] != "CORP":
        indexCorp += 1
"""



"""Estructuras de control"""

#Maneja condicionales de if
def metodo_if(linea, variables_loc):
    lineac = linea.removeprefix("if").removesuffix("fi")
    if linea.endswith("fi") == False:
        abort()
    # ( canWalk ( west ,1) ) { walk ( west ,1) }
    # ["canWalk ( west ,1)", "walk ( west ,1) }"]
    elif "else" in lineac:
        elseDef(lineac)
    else:
        ifNormal(lineac, variables_loc)

#Maneja if sencillo (una condicion y un bloque)
def ifNormal(lineac, variables_loc):
    vara = lineac.split("{")
    if len(vara) < 2:
        abort()
    else:
        if vara[0].startswith("(") == False or vara[0].startswith("(") == False:
            abort()
        else:
            cond = vara[0].removesuffix(")").removeprefix("(")
            condicion(cond)
        if vara[1].endswith("}") == False:
            abort()
        else:
            coman = vara[1].strip("}").split(";")
            comando(variables_loc, coman)

#Maneja if en caso de haber un else
def elseDef(linea, variables_loc):  # (else {})
    vari = linea.split("else")
    ifNormal(vari[0], variables_loc)
    if vari[1].startswith("{") == False or vari[1].startswith("}") == False:
        abort()
    else:
        limp = vari[1].removesuffix("}").removeprefix("{").split(";")
        comando(variables_loc, limp)

# Maneja while
def metodo_while(linea, variables_loc):
    varb = linea.removeprefix("while").removesuffix("od")
    # while ( canWalk ( north ,1) ) do { walk ( north ,1) } od
    # [( canWalk ( north ,1) ), walk ( north ,1)]
    if linea.endswith("od") == False or "do" not in varb:
        abort()
    else:
        varn = varb.split("do")
        condicion(varn[0])
        comando(variables_loc,varn[1].strip("{}".split(";")))

#Maneja repeat
def metodo_repeat(lon, variables_loc):
    if lon.endswith("per") == False:
        abort()
    else:
        perry = lon.removeprefix("repeatTimes").removesuffix("per").split("{")
        if len(perry) <2:
            abort()
        else:
            if perry[0].isnumeric()== False:
                isVar(perry[0])
            comando(variables_loc,perry[1].strip("}"))

"""Condicionales"""
def condicion(linea):
    if linea.startswith("isfacing"):
        facing(linea)
    elif linea.startswith("isValid"):
        valido(linea)
    elif linea.startswith("canWalk"):
        walk(linea)
    elif linea.startswith("not"):
        if len(linea.split("(")) < 2 or linea.endswith(")") == False:
            abort()
        else:
            eso = linea.remove("not").removesuffix(")").removeprefix("(")
            condicion(eso)

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
def comando(variables_loc, stringLista):
    for j in stringLista:
        if "(" in stringLista and ")" in stringLista:
            proc= j.split("(")
            if j.startswith("walk"):
                walk(j, None) 
            elif j.startswith("jump") or j.startswith("drop") or j.startswith("grab") or j.startswith("get") or j.startswith("free") or caso1(j, None):
                caso1(j, None)
            elif j.startswith("jumpTo"):
                caso2(j, None)
            elif j.startswith("veer")or j.startswith("look"):
                caso3(j)
            elif j.startswith("if"):
                metodo_if(j, variables_loc)
            elif j.startswith("while"):
                metodo_while(j, variables_loc)
            elif j.startswith("repeatTimes"):
                metodo_repeat(j, variables_loc)
            elif proc[0] in dic_PROC.keys():
                dicProc(j.removeprefix(proc[0]), proc[0])
        else:
            #revisar si es una asignacion
            dummy = False
            for v in variables_globales:
                if j.startswith(v):
                    dummy == True
            if dummy == False:
                abort()
            else:
                var1 = j.split(":=")
                if len(var1) == 1 or var1[1].isnumeric() == False:
                    abort()


def dicProc(lin, nom):
    num = dic_PROC[nom]
    if len(lin.split(","))!= num:
        abort()
    else:
        lini=lin.removeprefix("(").removesuffix(")").split(",")
        for l in lini:
            if l.isnumeric()==FALSE:
                abort()
    


# def comando(j):
#     if "(" in j and ")" in j:
#         if j.startswith("walk"):
#             walk(j, None) 
#         elif j.startswith("jump") or j.startswith("drop") or j.startswith("grab") or j.startswith("get") or j.startswith("free") or caso1(j, None):
#             caso1(j, None)
#         elif j.startswith("jumpTo"):
#             caso2(j, None)
#         elif j.startswith("veer")or j.startswith("look"):
#             caso3(j)
#     else:
#         abort()

# def controlStructure(j):
#     if j.startswith("if"):
#         metodo_if(j, None, None)
#     elif j.startswith("while"):
#         metodo_while(j, None, None)
#     elif j.startswith("repeatTimes"):
#         metodo_repeat(j, None)


def walk(linea, lista):

    var = linea.split("(")
    par = var[1].strip(")").split(",")
    if len(var[1].split(",")) == 1:
        caso1(linea, lista)
    elif len(var[1].split(",")) == 2:
        # ["walk",["d/o",n"]]
        if par[0] not in direcciones:
            if par[0] not in orientaciones:
                abort()
        elif par[1].isnumeric() == False:  # no es un número se verifica que es variable
            isVar(lista, par)
    elif len(var[1].split(",")) > 2:
        abort()


def valido(linea, lista):
    if "(" in linea and ")" in linea:
        var = linea.split("(")
        paras = var[1].strip(")").split(",")
        if len(var[1].split(",")) > 2:
            abort()
        else:
            if paras[0] not in ins:
                abort()
            elif paras[1].isnumeric() == False:  # no es un número se verifica que es variable (nombre o variable)
                isVar(lista, paras)
    else:
        abort()

def proc(bloque):
    variables_loc = primeralproc(bloque[0])
    listasin = bloque.pop(0)

    nombre_proc = bloque[0].remove("PROC").split("(")[0]

    string_bloque = ""
    for i in listasin:
        string_bloque += i
    string_bloque.replace(" ", "")
    if string_bloque.startswith("{") == False or string_bloque.endswith("}"):
        abort()
    stringLista = string_bloque.strip("{}").split(";")
    comando(variables_loc, stringLista, nombre_proc)

def bloque(bloq):
    string_bloque = ""
    for i in bloq:
        string_bloque += i
    string_bloque.replace(" ", "")
    if string_bloque.startswith("{") == False or string_bloque.endswith("}"):
        abort()
    else:
        stringLista = string_bloque.strip("{}").split(";")
        if string_bloque.count(";")!=len(stringLista)-1:
            abort()
        else:
            comando(None,stringLista)

            #[go(3,3)],[n=6],[putCB (2 ,1)]

        

#ENTRA UN STRING
def var(linea):
    leni= linea.replace(" ","").removeprefix("VAR") 
    #n, x, y; # se elimina el comando VAR
    if leni.endswith(";") ==False:  # si el ultimo caracter no es un punto y coma
        abort()
    else:
        varia = leni.removesufix(";").split(",")  # se separa la linea por comas
        if leni.count(",") != len(varia) - 1:  # si hay mas comas que variables
            abort()
        else:
            alphaNum(varia)
    return varia

#revisa q sea alfanumerico
def alphaNum(lista):
    for f in lista:
        if isalnum(f)==False or f[0].isalpha()==False:
            abort()

  # se sale del programa


##############################################
"""PROGRAMA PRINCIPAL"""
##############################################

with open("texto.txt", 'r') as f:  # se abre el archivo con el nombre texto.txt
    lines = f.readlines()  # se lee el archivo y se guarda en una lista

string_bloque = ""
for i in lines:
    string_bloque += i
string_bloque.replace(" ", "")

if string_bloque.count("{")%2>0 or string_bloque.count("}")%2>0 or string_bloque.count("(")%2>0 or string_bloque.count(")")%2>0: 
    # Revisa primera linea de programa
    if string_bloque.startswith("PROG") and string_bloque.endswith("GORP"):  # si la primera linea no es PROG se termina el programa
        i=1
        while(lines[i]!=NULL and i<len(lines[1:-1])): # Se salta la primera linea y última linea del archivo
            """PARTE A: VAR"""
            l=lines[i]
            if str(l).isspace() == False:  # si la linea no es un espacio se revisa si es una declaración de variables
                if l.startswith("VAR"):  # si la linea inicia con VAR se revisa si es una declaración de variables
                    variables_globales.append(var(l))  # se guardan las variables en una lista
                elif l.startswith("PROC"):
                    indexProc=i
                    indexCorp = -1
                    dummy=FALSE
                    for i in lines[indexProc+1:-1]:
                        if i.startswith("PROC"):
                            break
                        elif i.startswith("CORP"):
                            dummy=True
                            indexCorp= lines.index(i)
                            break
                    if dummy:
                        proc(lines[indexProc:indexCorp+1])
                    else:
                        abort()
                    i=indexCorp
                elif l.startswith("{"):
                    indexcorchi=lines.index(l)
                    indexcorchf = -1
                    dummy=FALSE
                    for i in lines[indexcorchi+1:-1]:
                        if i.startswith("{"):
                            break
                        elif i.startswith("}"):
                            dummy=True
                            indexcorchf= lines.index(i)
                            break
                    if dummy:
                        bloque(lines[indexcorchi:indexcorchf+1])
                    else:
                        abort()
                    i=indexcorchf
                else:
                    abort()
            i+=1
    else:
        abort()


    # indexProc, indexCorp = lines.index(l), lines.index(l)  # se obtiene el indice de la linea PROC
    # # se continua con el programa hasta encontrar una linea que inicie con CORP while
    # proc(l)
    # while lines[indexCorp] != "CORP":
    #     indexCorp += 1
# %%
a = ["{hsdhoid}","(sdfh)jhjh", "kjhgj", "kffl"]

for b in range(6):
    print(b)
    b=3






# %%
