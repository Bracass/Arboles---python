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
	

arbol = NodoN(10,[NodoN(20,[NodoN(40), NodoN(44)]),
				  NodoN(52,[NodoN(150)]),
				  NodoN(50),
				  NodoN(100,[NodoN(250),NodoN(500),NodoN(1000)])])

print (buscar_n(arbol, 10))
print (buscar_n(arbol, 1001))
#print (buscar_en_hijos([],20))
