import os
import sys
import json
import random
from tkinter import  filedialog
from GUI import *
from GUILogued import *
from GUIAdm import * 
from Matriz import *
from Matrizd import matriz
from PyQt5.QtWidgets import QDialog,QApplication,QFileDialog,QMainWindow,QWidget,QLabel,QMessageBox
from PyQt5.QtGui import QIcon,QPixmap
from Controlador import *
from Matriz import*
contador = 0
class GUIAPP(QDialog):
    def __init__(self):
     super().__init__()
     self.gui = Ui_MainWindow()
     self.gui.setupUi(self)
     self.gui.Login.clicked.connect(self.put)

     self.show()
    
    def put(self):
        usuario = self.gui.textEdit.toPlainText()
        contra = self.gui.textEdit_2.toPlainText()
        if usuario=="EDD" and contra == "edd123":
            self.ventana = QtWidgets.QMainWindow()
            GUIAdm = Ui_Admin()
            GUIAdm.setupUi(self.ventana)
            self.ventana.show()
        else:
            loguear(usuario,contra)

class GUIAPPLOGUED(QDialog):
    def __init__(self):
     super().__init__()
     self.logued = Ui_MainWindow2()
     self.logued.setupUi(self)
     self.show()

class GUIAPPAdm(QDialog):
    def __init__(self):
     super().__init__()
     self.adm = Ui_Admin()
     self.adm.setupUi(self)
     self.adm.Carga.clicked.connect(self.carga)
     self.adm.actionCarga.triggered.connect(self.carga)
     self.show()
     
    def carga(self):
        archivo = QFileDialog.getOpenFileName(self,"Abrir archivo","./","Archivos JSON (.json)")

        if archivo[0]:
            with open(archivo[0],"rt") as f:
                datos = f.read()
                

class GUIM(QDialog):
    def __init__(self):
     super().__init__()
     self.m = Ui_Me_Voy_A_Matar()
     self.m.setupUi(self)
     self.m.actionCargar.triggered.connect(self.carga)
     self.m.pushButton.clicked.connect(self.siguiente)
     self.show()
     contador = 0
    def carga(self):
        mat = matriz()
        ruta = filedialog.askopenfilename(title="Seleccione archivo", filetypes=[("Ficheros json", "*.json"), ("todos los archivos", "*.*")])
        contenido = None
        if (ruta != ""):
            with open(ruta, mode="r", encoding="utf-8") as file:
                contenido = json.load(file)
            a = int((contenido['tutorial']["ancho"]))

            mat.Agregarbarcos(a)
            
            for tutorial in contenido['tutorial']["movimientos"]:
                x = int((tutorial["x"]))
                y = int((tutorial["y"]))
                if (x < a and y < a):
                    mat.MarcarDisparo(x,y,a)
                elif (x > a and y < a):
                    x = a - random.randint(1,a-2)
                    mat.MarcarDisparo(x,y,a)
                elif (x < a and y > a):
                    y = a - random.randint(1,a-2)
                    mat.MarcarDisparo(x,y,a)
                else:
                    y = a - random.randint(1,a-2)
                    x = a - random.randint(1,a-2)
                    mat.MarcarDisparo(x,y,a)
        pixmap = QPixmap('./imagenes/Matriz_tutorial1.png')
        self.m.tablero.setPixmap(pixmap.scaled(600,600,aspectRatioMode=1))
        global contador 
        contador= contador+1
    def siguiente(self):
        global contador 
        contador = contador+1
        if (os.path.exists('./imagenes/Matriz_tutorial'+str(contador)+".png")==True):
                    pixmap = QPixmap('./imagenes/Matriz_tutorial'+str(contador)+'.png')
                    self.m.tablero.setPixmap(pixmap.scaled(600,600,aspectRatioMode=1))
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Advertencia")
            msg.setText("Ya no existe un disparo siguiente")
            x = msg.exec_()

def iniciar():
    app=QApplication(sys.argv)
    GUI = GUIM()
    GUI.show()
    sys.exit(app.exec_())

if __name__ == '__main__':

    iniciar()



