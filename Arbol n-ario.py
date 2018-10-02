class Nodo():
    def __init__(self,valor,izq=None,der=None):
        self.valor = valor
        self.izq = izq
        self.der = der


a1 = Nodo (25, Nodo (10), Nodo (50, Nodo (40)))

a2 = Nodo(15,Nodo(6, Nodo(4, Nodo(2), Nodo(3))),Nodo(50,Nodo(25),Nodo(104)))

a3 = Nodo (12, Nodo(8,Nodo(4),Nodo(10,Nodo(9),Nodo(11))), Nodo(25, Nodo(17), Nodo(30, Nodo(28), Nodo(50) ) )   )

#print (a2.der.izq.valor)


class Nario():
    def __init__(self,valor,nodos=[]):
        self.valor = valor
        self.nodos = nodos

an = Nario (2,[ Nario(4,[Nario(12), Nario(24), Nario(40)]), Nario(8,[Nario(16), Nario(32)]), Nario(5,[Nario(25), Nario(50)]) ] )
# problema es como entrar al otro nivel de la lista 

    
def contarNodo(arbol):
    if arbol == None:
        return 0
    return 1 + contarNodo(arbol.der) + contarNodo(arbol.izq)

def insertar(a,arbol):
    if arbol == None:
        arbol = Nodo(a)
    
    if  arbol.izq == None and arbol.der == None:
        if a<= arbol.valor:
            arbol.izq = Nodo(a)
        else:
            arbol.der= Nodo(a)
    else:
        if a<= arbol.valor:
            arbol = Nodo(arbol.valor,insertar(a,arbol.izq) )
        else:
            arbol= Nodo(arbol.valor, arbol.izq.valor,insertar(a,arbol.der))

def contarHoja(arbol):
    if arbol == None:
        return 0
    elif arbol.izq == None and arbol.der == None:
        return 1
    return contarHoja(arbol.izq) + contarHoja(arbol.der)
    
print ('hojas :',contarHoja(a3))

def contarElementos(arbol):
    if arbol == None:
        return 0
    elif arbol.izq == None and arbol.der == None:
        return 1
    return 1 + contarElementos(arbol.izq) + contarElementos(arbol.der)
print ('Elementos en arbol: ',contarElementos(a3))
#print ("de ",a3.izq.izq.der.valor)


def buscarEnArbol(n,arbol):
    if arbol==None:
        return False
    else:
        if n == arbol.valor:
            return True
        else:
            if n < arbol.valor:
                return buscarEnArbol(n,arbol.izq)
            else:
                return buscarEnArbol(n,arbol.der)
            

def in_orden(arbol):
    if arbol == None:
        return []
    return in_orden(arbol.izq) + [arbol.valor] + in_orden(arbol.der)


def postOrden(arbol):
    if arbol == None:
        return []
    return postOrden(arbol.izq) + postOrden(arbol.der) + [arbol.valor]
    
def preOrden(arbol):
    if arbol == None:
        return []
    return [arbol.valor] + preOrden(arbol.izq) + preOrden(arbol.der)


print ("En Inorden ",in_orden(a3))
print ("En PosOrden",postOrden(a3))
print ("En preOrden" ,preOrden(a3))
print ("inserto ", insertar(19,a3))
print "-----------------"
print ("En Inorden ",in_orden(a3))
print ("En PosOrden",postOrden(a3))
print ("En preOrden" ,preOrden(a3))
print "-----------------"
print buscarEnArbol(19,a3)
print ("Nodos: ",contarNodo(a3))

