from Doble_Items import nodo_items
from Doble_Items import doble_items
class nodo_usuario():

    def __init__(self,nombre,monedas,id,contrasena,edad,victorias) :
        
        self.nombre = nombre
        self.monedas = monedas
        self.id = id
        self.contrasena = contrasena
        self.edad = edad
        self.victorias = victorias
        self.tienda = doble_items()
        self.siguiente = None
        self.anterior = None