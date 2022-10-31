class nodo_items():

    def __init__(self,id,estado,nombre,categoria,precio,src) :


        self.id =id 
        self.estado = estado
        self.nombre =nombre
        self.categoria = categoria
        self.precio = precio
        self.src = src
        self.siguiente = None
        self.anterior = None