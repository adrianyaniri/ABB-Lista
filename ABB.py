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

    def insertarPagina(self, lista, web,pos = 0):
        if not lista.estaVacia() and pos < lista.len() :
            self.insertarPalabra(lista.getDato(pos),web)
            self.insertarPagina(lista, web, pos +1)


    def buscarPalabras(self, listaDePalabras):
        lista = Lista()
        if not self.estaVacio():
            lista = self.raiz.buscarPalabras(listaDePalabras)
        else:
            raise Exception('arbol vacio')   
        return lista



# funcion que retorna una lista de web de la palabra
    def listaWebPalabra(self, palabra):
        lista = Lista()
        if not self.estaVacio():
            lista = self.raiz.listaWebPalabra(palabra).clonar()
        else:
            raise Exception('arbol vacio')
           
        return lista


# funcion que recibe por parametro una web y retorna un lista con
# todas la palabras de esa pagina

    def palabrasDePagina(self, web):
        listaPalabras = Lista()
        if not self.estaVacio():
            self.raiz.palabrasDePagina(web,listaPalabras)
        else:
            raise Exception('arbol vacio')
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
        else:
            raise Exception('arbol vacio')


# elimina la pagina web de cada lista de palabras

    def eliminarPagina(self,web):
        if not self.estaVacio():
            self.raiz.eliminarPagina(web)
        else:
            raise Exception('arbol vacio')


# recibe por parametro un cantidad de letras
# buscar la cantidad de palabras que hay en el arbol
# con la misma cantidad o mas letras

    def cantidadTotalPalabras(self,cantidadLetras):
        total= 0
        if not self.estaVacio():
           total = self.raiz.cantidadTotalPalabras(cantidadLetras)
        else:
            raise Exception('arbol vacio')

        return total

# funcion que indica si el arbol esta balanceado o no

    def estaBalanceado(self):
        res = None
        if not self.estaVacio():
           res =  self.raiz.estaBalanceado(res)
        else:
            raise Exception('arbol vacio')
        return res



# falta eliminar la paginas repetitadas

    def paginasEnNivel(self,nivel):
        listaWeb = Lista()
        if not self.estaVacio():
           self.raiz.paginasEnNivel(nivel,listaWeb)
        else:
            raise Exception('arbol vacio')

        return listaWeb

    
    def cantidadDePalbrasMasUsadas(self, cantidadDePaginas):
        total = None
        if not self.estaVacio():
           total = self.raiz.cantidadDePalabrasMasUsadas(cantidadDePaginas)
        else:
            raise Exception ('arbol vacio')
        return total


# retorna un lista con todas la palabras que comienzan con mayuscla
#solo de los nodos internos
# no de los nodos hojas

    def internasMayusculasAlfabetico(self):
        lista = Lista()
        if not self.estaVacio():
            self.raiz.internasMayusculasAlfabetico(lista)
        else:
            raise Exception ('arbol vacio')
        return lista
