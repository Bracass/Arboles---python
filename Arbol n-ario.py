class NodoN:
	def __init__(self, valor, hijos = []):
		self.valor = valor
		self.hijos = hijos
	
def buscar_n(arbol, valor):
	if arbol == None:
		return False
	elif arbol.valor == valor:
		return True
	else:
		return buscar_en_hijos(arbol.hijos, valor)

def buscar_en_hijos(lista, valor):
	if lista == []:
		return False
	else:
		return buscar_n(lista[0], valor) or buscar_en_hijos(lista[1:], valor)
	


a1= NodoN(2,[NodoN(4,[NodoN(12,[]),NodoN(24,[]),NodoN(40,[])]),NodoN(8,[NodoN(16,[]),NodoN(32,[])]),NodoN(5,[NodoN(25,[]),NodoN(50,[])])])
print (buscar_n(a1, 10))
print (buscar_n(a1, 50))
