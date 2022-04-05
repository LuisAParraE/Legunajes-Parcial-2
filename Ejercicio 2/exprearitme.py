from decimal import DivisionByZero

expr = []

class node:
    def __init__(self,value, lchild,rchild):
        self.value = value
        self.lchild = lchild
        self.rchild = rchild

def menu():

    while True:

        entrada = input("Indique Instrucción: ")

        if entrada != "":
            
            instruccion = entrada.split()

            if instruccion[0] == "MOSTRAR":
                    
                if instruccion[1] == "PRE":
                    
                    tree = buildtree(instruccion[2:],"PRE")
                    printTree(tree)
                    print("")

                elif instruccion[1] == "POST":
                    
                    tree = buildtree(instruccion[2:],"POST")
                    printTree(tree)
                    print("")
                    
            elif instruccion[0] == "EVAL":

                if instruccion[1] == "PRE":

                    tree = buildtree(instruccion[2:],"PRE")
                    #printTree(tree)
                    resultado = int(Eval(tree))
                    print(f"El resultado es: {resultado}")

                elif instruccion[1] == "POST":

                    tree = buildtree(instruccion[2:],"POST")
                    #printTree(tree)
                    #print("")
                    resultado = int(Eval(tree))
                    print(f"El resultado es: {resultado}")

            elif instruccion[0] == "SALIR":
                break
    
def buildtree(Expresion,forma):
    global exp
    exp = Expresion

    if(forma == "PRE"):
         
        tree = node(exp.pop(0),buildPreTree(),buildPreTree())
        return tree

    else:

        tree = node(exp.pop(len(exp)-1),rchild = buildPostTree(),lchild = buildPostTree())
        return tree

def buildPreTree():
    global exp

    if len(exp) ==0:
        return None
    elif(exp[0] != '-' and exp[0]!= '+' and exp[0]!= '*' and exp[0]!= '/'):

        return node(exp.pop(0),None,None)
    else:

        tree = node(exp.pop(0),buildPreTree(),buildPreTree())
        return tree

def buildPostTree():
    global exp

    if len(exp) ==0:
        return None
    elif(exp[len(exp)-1] != '-' and exp[len(exp)-1]!= '+' and exp[len(exp)-1]!= '*' and exp[len(exp)-1]!= '/'):

        return node(exp.pop(len(exp)-1),None,None)
    else:

        tree = node(exp.pop(len(exp)-1),rchild = buildPostTree(),lchild = buildPostTree())
        return tree

def Eval(arbol):

    if(arbol.value  != '-' and arbol.value != '+' and arbol.value != '*' and arbol.value != '/'):
        return int(arbol.value)
    else:

        if(arbol.value == '+'):
            resultado = Eval(arbol.lchild) + Eval(arbol.rchild)
            return resultado
        elif(arbol.value == '-'):
            resultado = Eval(arbol.lchild) - Eval(arbol.rchild)
            return resultado
        elif(arbol.value == '*'):
            resultado = Eval(arbol.lchild) * Eval(arbol.rchild)
            return resultado
        elif(arbol.value == '/'):
            lchildresult = Eval(arbol.rchild)
            if(lchildresult == 0):
                print("Division por 0 no es valida")
                raise DivisionByZero
            else:
                resultado = Eval(arbol.lchild) / lchildresult
                return resultado

def printTree(arbol):

    if arbol.lchild != None:
        if((arbol.value == "/" or arbol.value == "*") and (arbol.lchild.value == "+" or arbol.lchild.value == "-")):
            print("( ",end="")
            printTree(arbol.lchild)
            print(" )",end="")
        else:
            printTree(arbol.lchild)

    print(" "+arbol.value+" ",end="")

    if arbol.rchild != None:
        if((arbol.value == "/" or arbol.value == "*") and (arbol.rchild.value == "+" or arbol.rchild.value == "-")):
            print("( ",end="")
            printTree(arbol.rchild)
            print(" )",end="")
        else:
            printTree(arbol.rchild)

menu()