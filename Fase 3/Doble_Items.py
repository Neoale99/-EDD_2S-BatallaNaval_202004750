from Nodo_Items import nodo_items
class doble_items():
    def __init__(self):
        self.primero = None
        self.ultimo = None
    def vacia(self):
        return self.primero == None
    def agregar(self,id,estado,nombre,categoria,precio,src):
        
        if self.vacia():
            self.primero = self.ultimo = nodo_items(id,estado,nombre,categoria,precio,src)
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = nodo_items(id,estado,nombre,categoria,precio,src)
            #self.ultimo = aux.siguiente
    def revisartienda(self):
        aux = self.primero
        while aux is not None:
            print(str(aux.id)+" "+aux.nombre)
            aux = aux.siguiente 
        return ""
    def comprar(self,id,nombre,tokens):
        aux = self.primero
        while aux is not None:
            print(id+" : "+str(aux.id)+" : "+aux.nombre+" : "+nombre)
            if aux.id == int(id) and aux.nombre == nombre:
                if tokens-aux.precio > 0:
                    print("Compraste algo")
                    aux.estado="Agotado"
                    return tokens-aux.precio                
            aux = aux.siguiente
        return False
    def cantidad(self):
        aux = self.primero
        i=0
        while aux is not None:
            i+=1
            aux = aux.siguiente 
        return i
    def retornaritem(self,tope):
        aux = self.primero
        i = 0
        while aux is not None:
            i+=1
            if i == tope:
                return(aux.nombre,aux.id,aux.precio,aux.categoria) 
            aux = aux.siguiente
    def comprados(self):
        aux = self.primero
        x = []
        while aux is not None:
            if aux.estado!="Disponible":
                x.append(aux.nombre+str(aux.id))
            aux = aux.siguiente
        return x

