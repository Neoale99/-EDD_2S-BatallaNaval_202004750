class nodo_barco():

    def __init__(self,tipo,estado,posx1,posx2,posx3,posx4,posy1,posy2,posy3,posy4,dir,vida) :


        self.tipo =tipo 
        self.estado = estado
        self.posx1 = posx1
        self.posx2 = posx2
        self.posx3 = posx3
        self.posx4 = posx4
        self.posy1 = posy1
        self.posy2 = posy2
        self.posy3 = posy3
        self.posy4 = posy4
        self.dir = dir
        self.vida = vida
        self.siguiente = None
        self.anterior = None
