from lista import*
from funcAux import*


class NodoArbol:

    def __init__(self, palabra = None , web = None):

        self.palabra = palabra
        self.izquierdo = None
        self.derecho = None
        self.paginas = Lista()
        self.paginas.append(web)

    def tieneIzquierdo(self):
        return self.izquierdo != None

    def tieneDerecho(self):
        return self.derecho != None

    def esHoja(self):
        return not self.tieneIzquierdo() and not self.tieneDerecho()

    def preOrden(self):
        print(self.palabra, self.paginas)
        if self.tieneIzquierdo():
            self.izquierdo.preOrden()
        if self.tieneDerecho():
            self.derecho.preOrden()

    def grado(self):
        grado = 0
        if self.tieneIzquierdo():
            grado += 1
        if self.tieneDerecho():
            grado += 1
        return grado

    def altura(self):
        altura = 0
        if self.grado() == 2:
            altura = 1 + max(self.izquierdo.altura() , self.derecho.altura())
        elif self.tieneIzquierdo():
            altura = 1 + self.izquierdo.altura()
        elif self.tieneDerecho():
            altura = 1 + self.derecho.altura()
        return altura



    def maximo(self):
        dato = None
        if self.tieneDerecho():
            dato = self.derecho.maximo()
        else:
            dato = self
        return self

    def predecesor(self):
        predecesor = None
        if self.tieneIzquierdo():
            predecesor = self.izquierdo.maximo()
        return predecesor

    def buscarElPadre(self,dato):
        hijo = None
        padre = None
        lado = None
        if dato < self.palabra:
            if self.tieneIzquierdo():
                if self.izquierdo.palabra == dato:
                    hijo = self.izquierdo
                    padre = self
                    lado = "izq"
                else:
                    hijo, padre , lado = self.izquierdo.buscarElPadre(dato)
        else:
            if self.tieneDerecho():
                if self.derecho.palabra == dato:
                    hijo = self.derecho
                    padre = self
                    lado = 'der'
                else:
                    hijo , padre , lado = self.derecho.buscarElPadre(dato)
        return hijo, padre, lado




# funcion que resive una palabra y una pagina web
# y la agrega al arbol
# si la palabra esta en el arbol solo agrega la pagina a la lista del nodo

    def insertarPalabra(self,nodo, web):

        if self.palabra == nodo.palabra:
            self.insertarWeb(web)

        elif nodo.palabra < self.palabra:
            if self.tieneIzquierdo():
                self.izquierdo.insertarPalabra(nodo,web)
            else:
                self.izquierdo = nodo
                nodo.insertarWeb(web)

        else:
            if self.tieneDerecho():
                self.derecho.insertarPalabra(nodo, web)
            else:
                self.derecho = nodo
                nodo.insertarWeb(web)

# funcion para agregar una pagina web en el nodo(palabra)
# compara si la web no esta en la lista del nodo, lo agrega a la lista
    def insertarWeb(self, web):
        if not self.paginas.estaEnLista(web):
            self.paginas.append(web)


    def buscarPalabras(self,listaDePalabras):
        if self.tieneIzquierdo():
            self.izquierdo.buscarPalabras(listaDePalabras)

        if self.tieneDerecho():
            self.derecho.buscarPalabras(listaDePalabras)


# retorna una lista web de la palabra pasado por parametro
    def listaWebPalabra(self, palabra):
        lista = Lista()
        if self.palabra == palabra:
            lista = self.paginas.clonar()
        else:
            if palabra < self.palabra:
                if self.tieneIzquierdo():
                    self.izquierdo.listaWebPalabra(palabra)
            else:
                if self.tieneDerecho():
                    self.derecho.listaWebPalabra(palabra)
        return lista


# funcion que recibe por parametro una web y un lista
# devuelve la lista con todas la palabras que esta en esa web
    def palabrasDePagina(self, web, listaPalabras = None) :

        if self.paginas.estaEnLista(web):
            listaPalabras.append(self.palabra)
        
        if self.tieneIzquierdo():
            self.izquierdo.palabrasDePagina(web, listaPalabras)

        if self.tieneDerecho():
            self.derecho.palabrasDePagina(web,listaPalabras)


# elimina la palabra que recibe por parametro

    def eliminarPalabra(self, palabra):
        palabraEliminar, padre,lado = self.buscarElPadre(palabra)
        if palabraEliminar != None:
            if palabraEliminar.grado() == 2:
                nodoPre = palabraEliminar.predecesor()
                self.eliminarPalabra(nodoPre.palabra)
                nodoPre.izquierdo = palabraEliminar.izquierdo
                nodoPre.derecho = palabraEliminar.derecho
                if lado == 'izq':
                    padre.izquierdo = nodoPre
                else:
                    padre.derecho = nodoPre
            elif palabraEliminar.tieneIzquierdo():
                if lado == 'izq':
                    padre.izquierdo = palabraEliminar.izquierdo
                else:
                    padre.derecho = palabraEliminar.izquierodo
            elif palabraEliminar.tieneDerecho():
                if lado == "izq":
                    padre.izquierdo = palabraEliminar.derecho
                else:
                    padre.derecho = palabraEliminar.derecho
            else:
                if lado == "izq":
                    padre.izquierdo = None
                else:
                    padre.derecho = None
                


# elimina la pagina web del arbol
#recibe por parametro un direccion web y la elimima de la lista de paginas de todas la palabras que estan en el arbol

    def eliminarPagina(self, web):

        if self.tieneIzquierdo():
            self.izquierdo.eliminarPagina(web)

        if self.tieneDerecho():
            self.derecho.eliminarPagina(web)

        if self.paginas.estaEnLista(web):
            self.paginas.deleteAll(web)
        

# recibe por parametro una cantidad de letras
# y retorna la cantidad de palabras del arbol
# que tienen la misma o mas cantidad

    def cantidadTotalPalabras(self,cantidadLetras):
        total = 0
        if self.tieneIzquierdo():
            total += self.izquierdo.cantidadTotalPalabras(cantidadLetras)

        if self.tieneDerecho():
            total += self.derecho.cantidadTotalPalabras(cantidadLetras)

        if cantidadLetras <= totalDeLetras(self.palabra):
            total += 1
        return total




# retorna true si la diferencia de altura entre
# la alturaIzq y la alturaDer , es menor o igual a 1


    def estaBalanceado(self, res):
        res = False
        alturaIzq = 0
        alturaDer = 0

        if self.tieneIzquierdo():
            alturaIzq += self.izquierdo.altura()

        if self.tieneDerecho():
            alturaDer += self.derecho.altura()
        
        if abs(alturaDer - alturaIzq) <= 1:
            res = True

        return res


# retorna las paginas que tiene en ese nivel del arbol

    def paginasEnNivel(self, nivel,listaWeb,nivelNodo = 0):
        if nivelNodo == nivel:
            listaWeb.append(self.paginas)
            
        else:
            if self.tieneIzquierdo():
                self.izquierdo.paginasEnNivel(nivel,listaWeb, nivelNodo +1)

            if self.tieneDerecho():
                self.derecho.paginasEnNivel(nivel,listaWeb, nivelNodo +1)



    
# retorna la cantidad de las palabras mas usas en todo el arbol
    def cantidadDePalabrasMasUsadas(self, cantidadDePaginas):
        cantidad = 0

        if self.tieneIzquierdo():
            cantidad += self.izquierdo.cantidadDePalabrasMasUsadas(cantidadDePaginas)

        if self.paginas.len() >= cantidadDePaginas:
            cantidad += 1

        if self.tieneDerecho():
            cantidad += self.derecho.cantidadDePalabrasMasUsadas(cantidadDePaginas)

        return cantidad

# retorna la lista con todas la palabras en mayusculas en orden alfabetico

    def internasMayusculasAlfabetico(self,lista):

        if self.tieneIzquierdo():
            self.izquierdo.internasMayusculasAlfabetico(lista)
        
        if not self.esHoja() and empiezaConMayuscula(self.palabra):
            lista.append(self.palabra)
        
        if self.tieneDerecho():
            self.derecho.internasMayusculasAlfabetico(lista)





        
        


    
            

