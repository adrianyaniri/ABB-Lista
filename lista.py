from nodoLista import*


class Lista:

    def __init__(self):

        self.primero = None

    def estaVacia(self):

        return self.primero == None

    def __repr__(self):

        out = 'primero'
        aux = self.primero
        while aux != None:
            out += ' -> ' + str(aux.dato)
            aux = aux.siguiente
        out += ' |'
        return out

    def append(self, dato):

        nodoNuevo = Nodo(dato)
        if self.estaVacia():
            self.primero = nodoNuevo
        else:
            self.primero.append(nodoNuevo)

    def len(self):
        cant = 0
        if not self.estaVacia():
            cant = self.primero.len()
        return cant

    def getDato(self, pos):
        dato = None
        if 0 <= pos < self.len() and not self.estaVacia():
            dato = self.primero.getDato(pos)
        else:
            raise Exception('posicion no valida')

    def deletePos(self, pos):

        if 0 <= pos < self.len() and not self.estaVacia():
            if pos == 0:
                self.primero = self.primero.siguiente
            else:
                self.primero.deletePos(pos)
        else:
            raise Exception('posicion no valida')

    def reemplazar(self, datoNuevo, datoViejo):
        if not self.estaVacia():
            self.primero.reemplazar(datoNuevo, datoViejo)
        else:
            raise Exception('lista esta vacia')

    def clonar(self):
        nuevaLista = Lista()
        if not self.estaVacia():
            self.primero.clonar(nuevaLista)
        else:
            raise Exception('lista vacia')
        return nuevaLista

    def delete(self, dato):
        if not self.estaVacia():
            if self.primero.dato == dato:
                self.primero = self.primero.siguiente
            else:
                self.primero.delete(dato)
        else:
            raise Exception('lista esta vacia')
    


# funcion que recibe por parametro un elemento y retorna si se encuentra o no en la lista
    def estaEnLista(self, elemento):
        res = False
        if not self.estaVacia():
            res = self.primero.estaEnLista(elemento)
        return res



    def obtenerElementos(self):
        aux = Lista()
        if not self.estaEnLista():
            self.primero.obtenerElementos(aux)
        else:
            raise Exception('lista vacia')
        return aux


# falta terminar
    def eliminarDuplicados(self):
        if not self.estaVacia():
            self.primero.eliminarDuplicados()




