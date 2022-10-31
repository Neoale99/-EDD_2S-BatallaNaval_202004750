from Nodo_usuarios import nodo_usuario

class doble_usuarios():
    def __init__(self):
        self.primero = None
        self.ultimo = None
    def vacia(self):
        return self.primero == None
    def agregar(self,nombre,monedas,id,contrasena,edad):
        
        if self.vacia():
            
            self.primero = self.ultimo = nodo_usuario(nombre,monedas,id,contrasena,edad,0)
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = nodo_usuario(nombre,monedas,id,contrasena,edad,0)
            #self.ultimo = aux.siguiente
    def revisar(self):
        aux = self.primero
        while aux is not None:
            print(aux.nombre+" "+aux.contrasena)
            aux = aux.siguiente 
    def login(self,nombre,contra):
        aux = self.primero
        while aux is not None:
            if aux.nombre == nombre and aux.contrasena == contra:
                return True
            aux = aux.siguiente
        return False
    def aumentavictoria(self,nombre,contra):
        aux = self.primero
        while aux is not None:
            if aux.nombre==nombre and aux.contrasena == contra:
                aux.victorias+=1
            aux = aux.siguiente
    def aumentatoken(self,nombre,contra,i):
        aux = self.primero
        while aux is not None:
            if aux.nombre==nombre and aux.contrasena == contra:
                x = 20 * i
                aux.monedas+=x
            aux = aux.siguiente
    def getid(self):
        aux = self.primero
        while aux is not None:
            if aux.siguiente == None:
                return aux.id
            aux = aux.siguiente
    def gettokens(self,nombre,contra):
        aux = self.primero
        
        while aux is not None:
            if aux.nombre==nombre and aux.contrasena == contra:
                return aux.monedas
            aux = aux.siguiente
    def actualizartokens(self,nombre,contra):
        aux = self.primero
        while aux is not None:
            if aux.nombre==nombre and aux.contrasena == contra:
                return aux.monedas
            aux = aux.siguiente
    def settienda(self,tienda):
        aux = self.primero
        while aux is not None:
            aux.tienda = tienda
            aux = aux.siguiente 
    def obtener(self,nombre,contra,id,nombrei):
        aux = self.primero
        
        while aux is not None:
   
            if aux.nombre==nombre and aux.contrasena == contra:
                aux.tienda.comprar(id,nombrei,aux.monedas)
                aux.tienda.revisartienda()
                x = (aux.tienda.comprar(id,nombrei,aux.monedas))
                aux.monedas = x
                return aux.tienda.comprados()
            aux = aux.siguiente


    def creartienda(self,nombre,contra):
        aux = self.primero
        while aux is not None:
            if aux.nombre==nombre and aux.contrasena == contra:
                aux.tienda.revisartienda()
            aux = aux.siguiente
    def getidhash(self,nombre,contra):
        aux = self.primero
        while aux is not None:
            if aux.nombre==nombre and aux.contrasena == contra:
                return aux.id
            aux = aux.siguiente