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

import sys  # se importa sys para poder usar sys.exit()

variables_globales = []  # se generan variables globales para poder usarlas en todo el programa
lista_PROC = []


def jump(linea):
    var = linea.split("(")


def jumpto(linea):
    var = linea.split("(")


def verr(linea):
    pass


def look(linea):
    pass


def drop(linea):
    pass


def get(linea):
    pass


def grab(linea):
    pass


def free(linea):
    pass


def pop(linea):
    pass


def walk(linea):
    pass


with open("texto.txt", 'r') as f:  # se abre el archivo con el nombre texto.txt
    lines = f.readlines()  # se lee el archivo y se guarda en una lista
    print(lines)

"""DEFINICIONES SECUNDARIAS"""


def proc(linea):
    variables_locales = []

    proc = linea.replace(" ", "").remove("PROC").split("(")  # lista separada PROC y resto de (nota!!!!!!: CASO PROC CB)
    if len(proc)== 1 or linea.endswith(")")== False:
        print("NO")
        sys.exit()

    lista_PROC[proc(0)] = len(proc(1).split(","))  # se extrae el nombre de la función y se mete por si se utiliza luego

    for x in proc(1).remove(")").split(","): # NOTA!!!: Hace falta revisar el caso de las comas
        variables_locales.append(x)

    indexProc, indexCorp = lines.index(l), lines.index(l)  # se obtiene el indice de la linea PROC
    # se continua con el programa hasta encontrar una linea que inicie con CORP while
    proc(l)
    while lines[indexCorp] != "CORP":
        indexCorp += 1


def var(linea):
    linea.delete("VAR")  # se elimina el comando VAR
    if linea[-1] != ";":  # si el ultimo caracter no es un punto y coma
        print("NO")
        sys.exit()  # se sale del programa
    varia = linea.split(",")  # se separa la linea por comas
    if linea.count(",") != len(varia) - 1:  # si hay mas comas que variables
        print("NO")
        sys.exit()  # se sale del programa
    return varia


def conditions():
    pass


"""PROGRAMA PRINCIPAL"""

# Revisa primera linea de programa
if lines[0] != "PROG\n":  # si la primera linea no es PROG se termina el programa
    print(lines[0])
    print("NO")
    sys.exit()

for l in lines[1:-1]:  # Se salta la primera linea y última linea del archivo
    """PARTE A: VAR"""
    if str(l).isspace() == False:  # si la linea no es un espacio se revisa si es una declaración de variables
        if l.startswith("VAR"):  # si la linea inicia con VAR se revisa si es una declaración de variables
            variables_globales.append(var(l))  # se guardan las variables en una lista

        if l.startswith("PROC"):
            proc_def = proc(l)

# Revisa la última liena del programa
if lines[-1] != "GORP":
    print(lines[-1])
    print("NO\n")
    sys.exit()
