# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUIAdm.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Admin(object):
    def setupUi(self, Admin):
        Admin.setObjectName("Admin")
        Admin.resize(674, 552)
        self.centralwidget = QtWidgets.QWidget(Admin)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 671, 551))
        self.label.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(220, 30, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.Carga = QtWidgets.QPushButton(self.centralwidget)
        self.Carga.setGeometry(QtCore.QRect(190, 90, 201, 41))
        self.Carga.setObjectName("Carga")
        self.G_Ab = QtWidgets.QPushButton(self.centralwidget)
        self.G_Ab.setGeometry(QtCore.QRect(190, 150, 201, 41))
        self.G_Ab.setObjectName("G_Ab")
        self.Asc = QtWidgets.QPushButton(self.centralwidget)
        self.Asc.setGeometry(QtCore.QRect(190, 210, 201, 41))
        self.Asc.setObjectName("Asc")
        self.Desc = QtWidgets.QPushButton(self.centralwidget)
        self.Desc.setGeometry(QtCore.QRect(190, 270, 201, 41))
        self.Desc.setObjectName("Desc")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(190, 320, 201, 41))
        self.pushButton_5.setObjectName("pushButton_5")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(420, 20, 241, 511))
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        Admin.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(Admin)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 674, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuCargar = QtWidgets.QMenu(self.menuBar)
        self.menuCargar.setObjectName("menuCargar")
        #Admin.setMenuBar(self.menuBar)
        self.actionCarga = QtWidgets.QAction(Admin)
        self.actionCarga.setObjectName("actionCarga")
        self.menuCargar.addAction(self.actionCarga)
        self.menuBar.addAction(self.menuCargar.menuAction())

        self.retranslateUi(Admin)
        QtCore.QMetaObject.connectSlotsByName(Admin)

    def retranslateUi(self, Admin):
        _translate = QtCore.QCoreApplication.translate
        Admin.setWindowTitle(_translate("Admin", "MainWindow"))
        self.label_2.setText(_translate("Admin", "Bienvenido"))
        self.Carga.setText(_translate("Admin", "Carga masiva"))
        self.G_Ab.setText(_translate("Admin", "Graficar arbol b"))
        self.Asc.setText(_translate("Admin", "Ordenar ascendente"))
        self.Desc.setText(_translate("Admin", "Ordenar Descendente"))
        self.pushButton_5.setText(_translate("Admin", "Salir"))
        self.menuCargar.setTitle(_translate("Admin", "Cargar"))
        self.actionCarga.setText(_translate("Admin", "Carga"))
        self.actionCarga.setShortcut(_translate("Admin", "Ctrl+Q"))
