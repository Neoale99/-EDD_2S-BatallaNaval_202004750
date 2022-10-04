import os
import random
import webbrowser
from Nodos import Nodo,NodoEncabezado
from Lista_cabecera import ListaEncabezado
P = 1
S = 2
D = 3
B = 4
contador = 0
contar = 0
class matriz:
    def __init__(self):
        self.filas = ListaEncabezado()
        self.columnas = ListaEncabezado()
    
    def insertar(self,fila,columna,estado,barco):
        nuevo = Nodo(fila,columna,estado,barco)
        eFila = self.filas.getEncabezado(fila)
        if eFila ==None:
            eFila = NodoEncabezado(fila)
            eFila.accesoNodo = nuevo
            self.filas.setEncabezado(eFila)
        
        else:
            if nuevo.columna < eFila.accesoNodo.columna:
                nuevo.right = eFila.accesoNodo
                eFila.accesoNodo.left = nuevo
                eFila.accesoNodo = nuevo
            
            else:
                actual = eFila.accesoNodo
                while actual.right != None:
                    if nuevo.columna < actual.right.columna:
                        nuevo.right = actual.right
                        actual.right.left = nuevo
                        nuevo.left = actual
                        actual.right = nuevo
                        break
                    actual = actual.right
                if actual.right == None:
                    actual.right = nuevo
                    nuevo.left = actual

        #---------------------------------------------------
        eColumna = self.columnas.getEncabezado(columna)
        if eColumna ==None:
            eColumna = NodoEncabezado(columna)
            eColumna.accesoNodo = nuevo
            self.columnas.setEncabezado(eColumna)
        
        else:
            if nuevo.fila < eColumna.accesoNodo.fila:
                nuevo.down = eColumna.accesoNodo
                eColumna.accesoNodo.up = nuevo
                eColumna.accesoNodo = nuevo
            
            else:
                actual = eColumna.accesoNodo
                while actual.down != None:
                    if nuevo.fila < actual.down.fila:
                        nuevo.down = actual.down
                        actual.down.up = nuevo
                        nuevo.up = actual
                        actual.down = nuevo
                        break
                    actual = actual.down
                if actual.down == None:
                    actual.down = nuevo
                    nuevo.up = actual

    def mostrarFilas(self):
        eFila = self.filas.primero
        print('--------FILAS---------')
        while eFila != None:
            actual = eFila.accesoNodo
            print('\n Fila ',actual.fila)
            print('Columna      Valor')
            
            while actual !=None:
                print(actual.columna,'          ',actual.estado)
                actual = actual.right

            eFila = eFila.next
        print('---------FIN----------')

    def mostrarColumnas(self):
        eColumna = self.columnas.primero

        while eColumna != None:
            actual = eColumna.accesoNodo
            print('\n Columna ',actual.columna)
            print('Fila      Valor')
            while(actual != None):
                print(actual.columna,",",actual.fila,'        ',actual.barco)
                actual = actual.down
            eColumna = eColumna.next
        print('---------FIN----------')
    def MarcarDisparo(self,x,y,tamano):
        if self.buscar(x,y)==False:
            self.insertar(y,x,"H","X")
        else:
            eColumna = self.columnas.primero
            while eColumna != None:
                actual = eColumna.accesoNodo
                while(actual != None):
                    if actual.columna==x and actual.fila==y:
                      actual.estado = "H"
                      print("Disparo registrado en: ("+str(x)+","+str(y)+")",actual.estado)
                    actual = actual.down
                eColumna = eColumna.next
            print('---------FIN----------')
        self.graficar(tamano)
    def Agregarbarcos(self,tamano): #dir representa la dirección del barco 0 = Vertical 1 = horizotal
        global contador,P,D,S,B
        if  contador==0:
            cantidad = int((((tamano-1)/10)+1))
            print(cantidad)      
            contador = contador+1   
            P = P*cantidad 
            S = S*cantidad 
            D = D*cantidad 
            B = B*cantidad 
            self.Agregarbarcos(tamano)
        else : 
            while P!=0:
                dir = random.randint(0,1)
                x = random.randint(1,tamano-4)
                y = random.randint(1,tamano-4)
                if self.Haybarco(x,y,dir,"P")==False:
                    if dir==0:
                        self.insertar(y,x,"L","P")
                        self.insertar(y+1,x,"L","P")
                        self.insertar(y+2,x,"L","P")
                        self.insertar(y+3,x,"L","P")
                        print("Agregado un portaviones")
                    else:
                        self.insertar(y,x,"L","P")
                        self.insertar(y,x+1,"L","P")
                        self.insertar(y,x+2,"L","P")
                        self.insertar(y,x+3,"L","P")
                        print("Agregado un portaviones")                        
                    P = P-1
                else: self.Agregarbarcos(tamano)
            while S!=0:
                dir = random.randint(0,1)
                x = random.randint(1,tamano-3)
                y = random.randint(1,tamano-3)
                if self.Haybarco(x,y,dir,"S")==False:
                    if dir==0:
                        self.insertar(y,x,"L","S")
                        self.insertar(y+1,x,"L","S")
                        self.insertar(y+2,x,"L","S")
                        print("Agregado un submarino")     
                    else:
                        self.insertar(y,x,"L","S")
                        self.insertar(y,x+1,"L","S")
                        self.insertar(y,x+2,"L","S")
                        print("Agregado un submarino")                       
                    S = S-1
                else: self.Agregarbarcos(tamano)
            while D!=0:
                dir = random.randint(0,1)
                x = random.randint(1,tamano-2)
                y = random.randint(1,tamano-2)
                if self.Haybarco(x,y,dir,"D")==False:
                    if dir==0:
                        self.insertar(y,x,"L","D")
                        self.insertar(y+1,x,"L","D")
                        print("Agregado un Destructor")     
                    else:
                        self.insertar(y,x,"L","D")
                        self.insertar(y,x+1,"L","D")
                        print("Agregado un Destructor")                       
                    D = D-1
                else: self.Agregarbarcos(tamano)
            while B!=0:
                dir = random.randint(0,1)
                x = random.randint(1,tamano)
                y = random.randint(1,tamano)
                if self.Haybarco(x,y,dir,"B")==False:
                    if dir==0:
                        self.insertar(y,x,"L","B")
                        print("Agregado un Buque")     
                    else:
                        self.insertar(y,x,"L","B")
                        print("Agregado un Buque")                       
                    B = B-1
                else: self.Agregarbarcos(tamano)                    

    def Haybarco(self,x,y,dir,tipo):
        i = 0

        if (tipo == "P"):
          if(dir ==0):
            while i <= 4:
                if self.buscar(x,y)==False:
                  y=y-1
                  i=i+1
                else:
                    return True
          else:
            while i <= 4:

                if self.buscar(x,y)==False:
                  x=x+1
                  i=i+1
                else:
                    return True
        elif (tipo == "S"):
          if(dir ==0):
            while i <= 3:
                if self.buscar(x,y)==False:
                  y=y-1
                  i=i+1
                else:
                    return True
          else:
            while i <= 3:

                if self.buscar(x,y)==False:
                  x=x+1
                  i=i+1
                else:
                    return True
        elif (tipo == "D"):
          if(dir ==0):
            while i <= 2:
                if self.buscar(x,y)==False:
                  y=y-1
                  i=i+1
                else:
                    return True
          else:
            while i <= 2:


                if self.buscar(x,y)==False:
                  x=x+1
                  i=i+1
                else:
                    return True
        elif (tipo == "B"):
          if(dir ==0):
            while i <= 1:
                if self.buscar(x,y)==False:
                  y=y-1
                  i=i+1
                else:
                    return True
          else:
            while i <= 1:

                if self.buscar(x,y)==False:
                  x=x+1
                  i=i+1
                else:
                    return True
        else:
            print("Esto no debería pasar")
        return False
    def buscar(self,x,y):
        eColumna = self.columnas.primero
        if eColumna==None:
            return False
        else:
            while eColumna != None:
                actual = eColumna.accesoNodo
                while(actual != None):
                    if actual.columna==x and actual.fila==y :
                        return True
                    actual = actual.down
                eColumna = eColumna.next    
            return False
    def graficar(self,tamano):
        global contar 
        contar = contar+1
        raiz = "raiz->F1 \nraiz->C1 "
        rCol ="{rank=same;raiz;"
        rF = ""
        Cabeceras = ""
        Uniones = ""
        for i in range(tamano):
            Cabeceras+="F"+str(i+1)+"[label=\""+str(i+1)+"\",group = 1]\n"
            Cabeceras+="C"+str(i+1)+"[label=\""+str(i+1)+"\",group = "+str(i+2)+"]\n"
            if (i+1==tamano):
                rCol +="C"+str(i+1)+"}\n"
            else: 
                rCol +="C"+str(i+1)+";"
                Uniones +="F"+str(i+1)+"->F"+str(i+2)+"\n"
                Uniones +="F"+str(i+1)+"->F"+str(i+2)+" [dir=back]\n"
                Uniones +="C"+str(i+1)+"->C"+str(i+2)+"\n"
                Uniones +="C"+str(i+1)+"->C"+str(i+2)+" [dir=back]\n"
        eColumna = self.columnas.primero
        Dir1 = ""
        Dir2 = ""
        Dir3 = ""
        #Dir4 = ""
        Nodos =""

        while eColumna != None:
            actual = eColumna.accesoNodo
            cont = 0
            while(actual != None):
                while cont!=1:
                  Dir1+="F"+str(actual.columna)+"->"
                  Dir2+="F"+str(actual.columna)+"->"
                  rF+= "{rank=same;F"+str(actual.columna)+";"
                  cont = cont+1
                if (actual.down == None):
                    Nodos+=("N"+str(actual.columna)+"_"+str(actual.fila)+"[label=\""+str(actual.columna)+","+str(actual.fila)+"("+actual.barco+")\",group = "+str(actual.fila+1)+",fillcolor="+self.colorbarco(actual.barco,actual.estado)+"]\n")
                    Dir1+=("N"+str(actual.columna)+"_"+str(actual.fila)+"")
                    Dir2+=("N"+str(actual.columna)+"_"+str(actual.fila)+"[dir=back]")
                    rF+="N"+str(actual.columna)+"_"+str(actual.fila)+"}"
                else:
                    Nodos+=("N"+str(actual.columna)+"_"+str(actual.fila)+"[label=\""+str(actual.columna)+","+str(actual.fila)+"("+actual.barco+")\",group = "+str(actual.fila+1)+",fillcolor="+self.colorbarco(actual.barco,actual.estado)+"]\n")
                    Dir1+=("N"+str(actual.columna)+"_"+str(actual.fila)+"->")
                    Dir2+=("N"+str(actual.columna)+"_"+str(actual.fila)+"->")
                    rF+="N"+str(actual.columna)+"_"+str(actual.fila)+";"
                actual = actual.down
            Dir1+= "\n"    
            Dir2+= "\n"    
            rF +="\n"
            eColumna = eColumna.next 
        #print(Nodos)
        eFila = self.filas.primero

        while eFila != None:
            actual = eFila.accesoNodo
            cont = 0
            while actual !=None:
                while cont!=1:
                    cont = cont+1
                    Dir3+="C"+str(actual.fila)+"->"
                    #Dir4+="C"+str(actual.fila)+"->"
                if (actual.right==None):
                    Dir3+=("N"+str(actual.columna)+"_"+str(actual.fila)+"")
                    #Dir4+=("N"+str(actual.columna)+"_"+str(actual.fila)+"[dir=back]")
                else:
                    Dir3+=("N"+str(actual.columna)+"_"+str(actual.fila)+"->")
                    #Dir4+=("N"+str(actual.columna)+"_"+str(actual.fila)+"->")
                actual = actual.right
            Dir3+="\n"
            #Dir4+="\n"
            eFila = eFila.next
        #print(Dir3)
        dot = "digraph G { \n  subgraph cluster_0 { \n       node[shape=box  fillcolor = \"Azure\" style = filled ] \n         label = \"Matriz dispersa\" \n         bgcolor = \"Skyblue\" \n         raiz[label = \"0,0\"] \n "
        dot+= (Cabeceras+Uniones+raiz+rCol+rF+Nodos+Dir1+Dir2+"edge [dir = both]\n"+Dir3+"\n}\n}")#Dir 4 quitado

        file = open("./imagenes/Matriz_tutorial.dot", "w")
        file.write(dot)
        file.close()
        
        os.system("dot -Tpng " + "./imagenes/Matriz_tutorial.dot" + " -o " + "./imagenes/Matriz_tutorial"+str(contar)+".png")
        
        

        file.close()
    def colorbarco(self,tipo,estado):
        if estado!="L":
            return "\"Red\""
        else:
            if tipo=="P":
                return "\"Maroon\""
            elif tipo=="S":
                return "\"#7B68EE\""
            elif tipo=="D":
                return "\"Gray\"" 
            elif tipo=="B": 
                return "\"#008080\""