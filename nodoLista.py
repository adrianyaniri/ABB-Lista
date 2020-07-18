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
                self.siguiente.delete(dato)
            

# recibe un nodo y busca en la lista si esta el elemento pasado por parametro
# retorna 'true' si lo encuentra

    def estaEnLista(self, elemento):
        res = False
        if self.tieneSiguiente():
            if self.siguiente.dato == elemento:
                res = True
            else:
                res = self.siguiente.estaEnLista(elemento)

        return res


# recibe por parametro un nodo y retorna el nodo en esa posicion
    def getNodo(self,pos,posAct = 0):
        nodo = None
        if posAct == pos:
            nodo = self
        else:
            nodo = self.siguiente.getNodo(pos, posAct + 1)
        return nodo



        
