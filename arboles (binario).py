class Nodo():
    def __init__(self,valor,izq=None,der=None):
        self.valor = valor
        self.izq = izq
        self.der = der


a1 = Nodo (12, Nodo (8,Nodo(4),Nodo(10,Nodo(9),Nodo(11))), Nodo(25,Nodo(17),Nodo(30,Nodo (28),Nodo(50))))

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
            
def contarNodo(arbol):
    if arbol == None:
        return 0
    elif arbol.izq == None and arbol.der == None:
        return 0
    return 1 + contarNodo(arbol.der) + contarNodo(arbol.izq)

def contarHoja(arbol):
    if arbol == None:
        return 0
    elif arbol.izq == None and arbol.der == None:
        return 1
    return contarHoja(arbol.izq) + contarHoja(arbol.der)
            
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


def enOrden(arbol):
    if arbol == None:
        return []
    return enOrden(arbol.izq) + [arbol.valor] + enOrden(arbol.der)

def  posOrden(arbol):
    if arbol == None:
        return []
    return posOrden(arbol.izq) + posOrden(arbol.der) +[arbol.valor]
def preOrden(arbol):
    if arbol==None:
        return []
    return [arbol.valor] + preOrden(arbol.izq) + preOrden(arbol.der)

    
print (enOrden(a1))
print (posOrden(a1))
print (preOrden(a1))
print (buscarEnArbol(12,a1))
print 'Nodos : ',contarNodo(a1)
print 'Hojas: ',contarHoja(a1)
print 'Valor insertado', insertar(16,a1)
print 'Nodos: ', contarNodo(a1)
print 'Hojas: ',contarHoja(a1)
print (preOrden(a1))

