class Nodo:
    
    def __init__(self, dato):

        self.dato = dato
        self.siguiente = None

    def tieneSiguiente(self):

        return self.siguiente != None

    def append(self, nodoNuevo):

        if self.tieneSiguiente():
            self.siguiente.append(nodoNuevo)
        else:
            self.siguiente = nodoNuevo

    def len(self):
        cant = 1
        if self.tieneSiguiente():
            cant += self.siguiente.len()
        return cant

    def getDato(self, getPos, posAct = 0):
        dato = None
        if posAct == getPos:
            dato = self.dato
        else:
            dato = self.siguiente.getDato(getPos, posAct+1)
        return dato

    def deletePos(self, posDel, posAct = 0):
        if posAct == posDel -1:
            self.siguiente = self.siguiente.siguiente
        else:
            self.siguiente.deletePos(posDel, posAct+1)



    def reemplazar(self, nuevo, viejo):
        if self.dato == viejo:
            self.dato = nuevo
        if self.tieneSiguiente():
            self.siguiente.reemplazar(nuevo, viejo)


    def clonar(self, nuevaLista):
        nuevaLista.append(self.dato)
        if self.tieneSiguiente():
            self.siguiente.clonar(nuevaLista)
        return nuevaLista


    def delete(self, dato):
        if self.tieneSiguiente():
            if self.siguiente.dato == dato:
                self.siguiente = self.siguiente.siguiente
            else:
                self.siguiente.deleteAll(dato)
            

# recibe un nodo y busca en la lista si esta el elemento pasado por parametro
# retorna 'true' si lo encuentra

    def estaEnLista(self, elemento):
        res = None
        if self.dato == elemento:
            res = True
        else:
            if self.siguiente != None:
                self.siguiente.estaEnLista(elemento)
            res = False
        return res




    def eliminarDuplicados(self):
        if self.tieneSiguiente():
            if self.dato == self.siguiente.dato:
                self.siguente = self.siguiente.siguiente
                self.delete(self.siguiente)
            else:
                self.siguiente.eliminarDuplicados()
        
            


