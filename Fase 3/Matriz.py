from ast import Global
import os
import random
from tkinter import messagebox
from Nodos import Nodo,NodoEncabezado
from Lista_cabecera import ListaEncabezado
from Doble import doble

contar = 0
Barcos_restantes = 0
tamanot = 0
dob = doble()
class matriz:

    def __init__(self):
        self.filas = ListaEncabezado()
        self.columnas = ListaEncabezado()
        self.P = 1
        self.S = 2
        self.D = 3
        self.B = 4
        self.contador = 0
        self.Barcos_restantes = 0
        self.tamanot=0
        self.dob = dob
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
                print(actual.columna,",",actual.fila,'        ',actual.estado)
                actual = actual.down
            eColumna = eColumna.next
        print('---------FIN----------')
    def MarcarDisparo(self,x,y,tamano):
        if x > tamano or y > tamano:
            messagebox.showinfo("Error","Ingrese coordenadas validas")
            return
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
                      self.ComprobarBarcos(x,y)
                    actual = actual.down
                eColumna = eColumna.next
            print('---------FIN----------')

        
    def Agregarbarcos(self,tamano): #dir representa la dirección del barco 0 = Vertical 1 = horizotal
        self.tamanot = tamano
        
        
        if  self.contador==0:
            cantidad = int((((tamano-1)/10)+1))
            print(cantidad)      
            self.contador = self.contador+1   
            self.P = self.P*cantidad 
            self.S = self.S*cantidad 
            self.D = self.D*cantidad 
            self.B = self.B*cantidad 
            self.Agregarbarcos(tamano)
        else : 
            while self.P!=0:
                dir = random.randint(0,1)
                x = random.randint(1,tamano-4)
                y = random.randint(1,tamano-4)
                if self.Haybarco(x,y,dir,"P")==False:
                    if dir==0:
                        self.insertar(y,x,"L","P")
                        self.insertar(y+1,x,"L","P")
                        self.insertar(y+2,x,"L","P")
                        self.insertar(y+3,x,"L","P")
                        dob.agregar("P","Vivo",x,0,0,0,y,y+1,y+2,y+3,0,4)
                        
                        self.Barcos_restantes +=1
                    else:
                        self.insertar(y,x,"L","P")
                        self.insertar(y,x+1,"L","P")
                        self.insertar(y,x+2,"L","P")
                        self.insertar(y,x+3,"L","P")
                        dob.agregar("P","Vivo",x,x+1,x+2,x+3,y,0,0,0,1,4)
                           
                        self.Barcos_restantes +=1                    
                    self.P = self.P-1
                else: self.Agregarbarcos(tamano)
            while self.S!=0:
                dir = random.randint(0,1)
                x = random.randint(1,tamano-3)
                y = random.randint(1,tamano-3)
                if self.Haybarco(x,y,dir,"S")==False:
                    if dir==0:
                        self.insertar(y,x,"L","S")
                        self.insertar(y+1,x,"L","S")
                        self.insertar(y+2,x,"L","S")
                        dob.agregar("S","Vivo",x,0,0,0,y,y+1,y+2,0,0,3)
                        
                        self.Barcos_restantes +=1     
                    else:
                        self.insertar(y,x,"L","S")
                        self.insertar(y,x+1,"L","S")
                        self.insertar(y,x+2,"L","S")
                        dob.agregar("S","Vivo",x,x+1,x+2,0,y,0,0,0,1,3)
                        
                        self.Barcos_restantes +=1                       
                    self.S = self.S-1
                else: self.Agregarbarcos(tamano)
            while self.D!=0:
                dir = random.randint(0,1)
                x = random.randint(1,tamano-2)
                y = random.randint(1,tamano-2)
                if self.Haybarco(x,y,dir,"D")==False:
                    if dir==0:
                        self.insertar(y,x,"L","D")
                        self.insertar(y+1,x,"L","D")
                        dob.agregar("D","Vivo",x,0,0,0,y,y+1,0,0,0,2)
                        
                        self.Barcos_restantes +=1     
                    else:
                        self.insertar(y,x,"L","D")
                        self.insertar(y,x+1,"L","D")
                        dob.agregar("D","Vivo",x,x+1,0,0,y,0,0,0,1,2)
                        
                        self.Barcos_restantes +=1                       
                    self.D = self.D-1
                else: self.Agregarbarcos(tamano)
            while self.B!=0:
                dir = random.randint(0,1)
                x = random.randint(1,tamano)
                y = random.randint(1,tamano)
                if self.Haybarco(x,y,dir,"B")==False:
                    if dir==0:
                        self.insertar(y,x,"L","B")
                        dob.agregar("B","Vivo",x,0,0,0,y,0,0,0,0,1)
                        
                        self.Barcos_restantes +=1     
                    else:
                        self.insertar(y,x,"L","B")
                        dob.agregar("B","Vivo",x,0,0,0,y,0,0,0,0,1)
                        
                        self.Barcos_restantes +=1                       
                    self.B = self.B-1
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
    def buscar_T(self,x,y):
        eColumna = self.columnas.primero
        if eColumna==None:
            return False
        else:
            while eColumna != None:
                actual = eColumna.accesoNodo
                while(actual != None):
                    if actual.columna==x and actual.fila==y :
                        return actual.estado
                    actual = actual.down
                eColumna = eColumna.next    
            return False
    def buscar_T2(self,x,y):
        eColumna = self.columnas.primero
        if eColumna==None:
            return False
        else:
            while eColumna != None:
                actual = eColumna.accesoNodo
                while(actual != None):
                    if actual.columna==x and actual.fila==y :
                        return actual.barco
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

        file = open("./imagenes/Matriz_puta.dot", "w")
        file.write(dot)
        file.close()
        
        os.system("dot -Tpng " + "./imagenes/Matriz_puta.dot" + " -o " + "./imagenes/Matriz_puta"+str(contar)+".png")
        
        #webbrowser.open("./imagenes/Matriz_puta"+str(contar)+".png")

        file.close()
    def tablero(self,tamano,nombre):
        cabecera = """digraph tablero {
                        node [fontcolor="white"]
                        tabla [shape = none, margin = 0, label=<
                        <TABLE BORDER = "1" CELLBORDER = "1" CELLSPACING="0" CELLPADDING="10" style='rounded'>
                        <TR>
                        <TD > </TD>"""
        cuerpo = ""
        for i in range (tamano):
            cuerpo+=("<TD BGCOLOR=\"DarkTurquoise\">"+str(i+1)+"</TD>\n")
        cuerpo+=("</TR>\n")
        for i in range(tamano):
            for j in range(tamano):
                if j ==0:
                    cuerpo+=("<TR> \n <TD BGCOLOR=\"DarkTurquoise\">"+str(i+1)+"</TD>\n")
                color = self.colorbarco(self.buscar_T2(i+1,j+1),self.buscar_T(i+1,j+1))
                acompana = ""
                if self.buscar_T2(i+1,j+1)!= False:
                    acompana = self.buscar_T2(i+1,j+1)
                elif self.buscar_T(i+1,j+1)!= False:
                    acompana = self.buscar_T(i+1,j+1)
                else:
                    acompana = ""
                    
                cuerpo+=("<TD BGCOLOR="+color+">"+str(i+1)+","+str(j+1)+"("+acompana+")"+"</TD>\n")  #Copiar colorbarco para hacer el BGCOLOR
                if j+1==tamano:
                    cuerpo+=("</TR>\n")
        
        fin ="""</TABLE>>];
            }"""
        dot = cabecera+cuerpo+fin
        file = open("./imagenes/tablero"+nombre+".dot", "w")
        file.write(dot)
        file.close()
        
        os.system("dot -Tpng " + "./imagenes/tablero"+nombre+".dot" + " -o " + "./imagenes/tablero"+nombre+".png")

    def colorbarco(self,tipo,estado):
        if estado == False:
            return "\"White\""
        if estado=="H":
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
    def ComprobarBarcos(self,x,y): #Revisar retorna x,y,dir
        
        if dob.revisar(x,y) == 1: #Usar este método para el reporte de barcos destruidos, cambiando el return por un string
            self.Barcos_restantes = self.Barcos_restantes-1
            print("Barcos restantes = " + str(self.Barcos_restantes))
            if self.Barcos_restantes == 16:
                messagebox.showinfo("Info","Victoria!")
                self.ListaAdyacencia()
                self.Grafo()
                return 1
    def victoria(self):

        if self.Barcos_restantes==0:
            
            return 1
        else: return 0
    def comprobargolpes(self):
        eFila = self.filas.primero
        i = 0
        while eFila != None:
            actual = eFila.accesoNodo
            while actual !=None:
                if actual.estado=="H" and actual.barco !="X":
                    i+=1   
                actual = actual.right
            eFila = eFila.next
        return i
    def ListaAdyacencia(self):
        tamano = self.tamanot
        nodosc = ""
        nodos = ""
        i = 1
        eColumna = self.columnas.primero
        while eColumna != None:
            actual = eColumna.accesoNodo
            nodosc+= "\t\t\t n"+str(i)
            nodos+= "\t\t\t n"+str(i)+"[label =\""+str(i)+"\"]\n"
            while(actual != None):
                #print(actual.columna,",",actual.fila,'        ',actual.estado)
                if actual.estado =="H":
                    nodosc+="->"+"n"+str(actual.fila)+"_"+str(actual.columna)
                    nodos+="\t\t\t n"+str(actual.fila)+"_"+str(actual.columna)+"[label =\""+str(actual.fila)+"\"]\n"
                if actual.down == None:
                    nodosc+="[color = \"#172A3A\"];\n"
                actual = actual.down
            
            
            i=i+1
            eColumna = eColumna.next
        if i<tamano+1:
            while i< tamano+1:
                nodosc+="n"+str(i)+"\n"
                nodos+="n"+str(i)+"[label =\""+str(i)+"\"]"+"\n"
                i=i+1
        encabezado="""
        digraph G {
            rankdir=LR
            compound = true;
            labelloc="t";
            bgcolor = "#508991";
            fontcolor = Black;
            color = "#004346"

        subgraph cluster_0 {
            node [style=filled,shape=note,fillcolor="#74b3ce",color = "#172A3A"];
            label = "Lista de adyacencia"
        """
        dot = encabezado+nodosc+nodos+"\n} \n}"
        file = open("./imagenes/Lista_Adyacencia.dot", "w")
        file.write(dot)
        file.close()
        
        os.system("dot -Tpng " + "./imagenes/Lista_Adyacencia.dot" + " -o " + "./imagenes/Lista_Adyacencia.png")
    def Grafo(self):
        tamano = self.tamanot
        encabezado="""digraph G {
    subgraph cluster_0 {
    style=filled;
    color="#0BC9CD";
    node [style=filled,color=white,shape=ellipse,color="#8FBFE0"];
    edge [color="#7C77B9"]
    rankdir = LR
    label=\"Grafo tiros del ganador\""""
        grafo = ""
        i = 1
        eColumna = self.columnas.primero
        while eColumna != None:
            actual = eColumna.accesoNodo
            while(actual != None):
                if actual.estado =="H":
                    grafo+="\t"+str(i)+"->"+str(actual.fila)+"\n"
                actual = actual.down
            i=i+1
            eColumna = eColumna.next
        dot = encabezado+grafo+"\n} \n}"
        file = open("./imagenes/grafo.dot", "w")
        file.write(dot)
        file.close()
        
        os.system("dot -Tpng " + "./imagenes/grafo.dot" + " -o " + "./imagenes/grafo.png")