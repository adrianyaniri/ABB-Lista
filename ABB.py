from nodoABB import*
from lista import*
from funcAux import*


class ABB:
    
    def __init__(self):
        self.raiz = None

  # funcion para saber si el arbol esta vacio

    def estaVacio(self):
        return self.raiz == None

    def preOrden(self):
        if not self.estaVacio():
            self.raiz.preOrden()
        else:
            print("Arbol vacio.")

    def maximo(self):
        maximo = None
        if not self.estaVacio():
            maximo = self.raiz.maximo().palabra

    def profundidad(self):
        porf = 0
        if not self.estaVacio():
            prof = self.raiz.altura()
        return prof


# insetar una palabra y una web el arbol de busqueda
# si es el arbol esta vacio crea el nodo y agrega la palabra

    def insertarPalabra(self, palabra, web):
        nuevoNodo = NodoArbol(palabra,web)
        if self.estaVacio():
            self.raiz = nuevoNodo
        else:
            self.raiz.insertarPalabra(nuevoNodo,web)

# funcion que recibe por parametro un lista de palabras y una web.
# las inserta en el arbol donde corresponda

    def insertarPagina(self, listaPaginas, web):
        aux = listaPaginas.primero
        while aux != None:
            self.insertarPalabra(aux.dato, web)
            aux = aux.siguiente

    def buscarPalabras(self, listaPalabras):
        listaWeb = Lista()
        if not self.estaVacio():
            self.raiz.buscarPalabras(listaPalabras)


    def listaWebsDeLaPalabra(self,palabra):
        listaAux = Lista()
        if not self.estaVacio():
            self.raiz.listaWebsDeLaPalabra(palabra, listaAux)
        listaAux = palabra.clonar()
        return listaAux


# funcion que recibe por parametor una web y retorna un lista con
# todas la palabras de esa pagina

    def palabrasDePagina(self, web):
        listaPalabras = Lista()
        if not self.estaVacio():
            self.raiz.palabrasDePagina(web,listaPalabras)
        return listaPalabras

# recibe por parametro una palabra y la elimina del arbol
    def eliminarPalabra(self,palabra):
        if not self.estaVacio():
            if palabra == self.raiz.palabra:
                if self.raiz.grado == 2:
                    nodoPre = self.raiz.predecesor()
                    self.eliminarPalabra(nodoPre.palabra)
                    nodoPre.izquierdo = self.raiz.izquierdo
                    nodoPre.derecho = self.raiz.derecho
                    self.raiz = nodoPre
                elif self.raiz.tieneIzquierdo():
                    self.raiz = self.raiz.izquierdo
                elif self.raiz.tieneDerecho():
                    self.raiz = self.raiz.derecho
                else:
                    self.raiz = None
            else:
                self.raiz.eliminarPalabra(palabra)


# elimina la pagina web de cada lista de palabras

    def eliminarPagina(self,web):
        if not self.estaVacio():
            self.raiz.eliminarPagina(web)


# recibe por parametro un cantidad de letras
# buscar la cantidad de palabras que hay en el arbol
# con la misma cantidad o mas letras

    def cantidadTotalPalabras(self,cantidadLetras):
        total= 0
        if not self.estaVacio():
           total = self.raiz.cantidadTotalPalabras(cantidadLetras)
        return total

# funcion que indica si el arbol esta balanceado o no

    def estaBalanceado(self):
        res = None
        if not self.estaVacio():
           res =  self.raiz.estaBalanceado(res)
        return res



# falta eliminar la paginas repetitadas

    def paginasEnNivel(self,nivel):
        lista = Lista()
        if not self.estaVacio():
          self.raiz.paginasEnNivel(nivel, lista)

        return lista

    
    def cantidadDePalbrasMasUsadas(self, cantidadDePaginas):
        total = None
        if not self.estaVacio():
           total = self.raiz.cantidadDePalabrasMasUsadas(cantidadDePaginas)
        return total



abb = ABB()
abb.insertarPalabra('tarro','google')
abb.insertarPalabra('dado','yahoo')
abb.insertarPalabra('fuente','google')

l = Lista()
l.append('sabana')
l.append('te')
l.append('oso')
l.append('foca')
l.append('vampiro')

abb.insertarPagina(l,'google')
abb.insertarPalabra('tarro', 'yahoo')
abb.insertarPagina(l,'get')

print(abb.preOrden())
print(abb.cantidadDePalbrasMasUsadas(2))