import os
from Nodo_Barcos import nodo_barco

class doble():
    def __init__(self):
        self.primero = None
        self.ultimo = None


    def vacia(self):
        return self.primero == None

    def agregar(self,tipo,estado,posx1,posx2,posx3,posx4,posy1,posy2,posy3,posy4,dir,vida):
        
        if self.vacia():
            
            self.primero = self.ultimo = nodo_barco(tipo,estado,posx1,posx2,posx3,posx4,posy1,posy2,posy3,posy4,dir,vida)
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = nodo_barco(tipo,estado,posx1,posx2,posx3,posx4,posy1,posy2,posy3,posy4,dir,vida)
            #self.ultimo = aux.siguiente
    
    def revisar(self,x,y):
        aux = self.primero
        i = 0
        while aux is not None:
            i = i+1

            if x == aux.posx1 and y == aux.posy1:
                aux.vida = aux.vida-1
                print(aux.vida)
                if aux.vida == 0:
                    return 1
                else:
                    return 0
            elif x == aux.posx1 and y == aux.posy2:
                aux.vida = aux.vida-1
                print(aux.vida)
                if aux.vida == 0:
                    return 1
                else:
                    return 0
            elif x == aux.posx1 and y == aux.posy3:
                aux.vida = aux.vida-1
                print(aux.vida)
                if aux.vida == 0:
                    return 1
                else:
                    return 0
            elif x == aux.posx1 and y == aux.posy4:
                aux.vida = aux.vida-1
                print(aux.vida)
                if aux.vida == 0:
                    return 1
                else:
                    return 0
            elif x == aux.posx1 and y == aux.posy1:
                aux.vida = aux.vida-1
                print(aux.vida)
                if aux.vida == 0:
                    return 1
                else:
                    return 0
            elif x == aux.posx2 and y == aux.posy1:
                aux.vida = aux.vida-1
                print(aux.vida)
                if aux.vida == 0:
                    return 1
                else:
                    return 0
            elif x == aux.posx3 and y == aux.posy1:
                aux.vida = aux.vida-1
                print(aux.vida)
                if aux.vida == 0:
                    return 1
                else:
                    return 0
            elif x == aux.posx4 and y == aux.posy1:
                aux.vida = aux.vida-1
                print(aux.vida)
                if aux.vida == 0:
                    return 1
                else:
                    return 0
            else:
                pass

            aux = aux.siguiente
    def Destruidos(self,nombre):
        aux = self.primero
        p = 0
        s = 0
        d = 0
        b = 0
        while aux is not None:
            if aux.vida == 0:
                if aux.tipo == "P":
                    p+=1
                elif aux.tipo =="S":
                    s+=1
                elif aux.tipo =="D":
                    d+=1
                elif aux.tipo =="B":
                    b+=1
            aux = aux.siguiente
        dot = """digraph ReporteG {
    node [fontcolor="white",shape = none]
    tabla [shape = none, margin = 0, label=<
    <TABLE BORDER = "4" CELLBORDER = "1" CELLSPACING="4">
    <TR> <TD BGCOLOR="#5E503F">Reporte """+nombre+"""</TD> </TR>
    <tr><td cellpadding='4'>
    <table color='#F2F4F3' cellspacing='0'>
    <TR>
    <TD BGCOLOR = "#A9927D">Barcos destruidos</TD> <TD BGCOLOR = "#A9927D"> Tipo de barco</TD>
    </TR>
    <TR>
    <TD BGCOLOR = "#BDA78A">Portaaviones</TD> <TD BGCOLOR = "#BDA78A"> """+str(p)+"""</TD>
    </TR>
    <TR>
    <TD BGCOLOR = "#BDA78A">Submarinos</TD> <TD BGCOLOR = "#BDA78A"> """+str(s)+"""</TD>
    </TR>
    <TR>
    <TD BGCOLOR = "#BDA78A">Destructores</TD> <TD BGCOLOR = "#BDA78A"> """+str(d)+"""</TD>
    </TR>
    <TR>
    <TD BGCOLOR = "#BDA78A">Buques</TD> <TD BGCOLOR = "#BDA78A"> """+str(b)+"""</TD>
    </TR>
    </table>
    </td> 
    </tr>
    </TABLE>>];
    }"""
        file = open("./imagenes/reporte"+nombre+".dot", "w")
        file.write(dot)
        file.close()
        os.system("dot -Tpng " + "./imagenes/reporte"+nombre+".dot" + " -o " + "./imagenes/reporte"+nombre+".png")
