# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'matriz.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Me_Voy_A_Matar(object):
    def setupUi(self, Me_Voy_A_Matar):
        Me_Voy_A_Matar.setObjectName("Me_Voy_A_Matar")
        Me_Voy_A_Matar.resize(900, 700)
        self.centralwidget = QtWidgets.QWidget(Me_Voy_A_Matar)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(650, 35, 191, 41))
        self.pushButton.setObjectName("pushButton")
        self.tablero = QtWidgets.QLabel(self.centralwidget)
        self.tablero.setGeometry(QtCore.QRect(20, 70, 600, 600))
        self.tablero.setText("")
        self.tablero.setObjectName("tablero")
        #Me_Voy_A_Matar.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Me_Voy_A_Matar)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 847, 21))
        self.menubar.setObjectName("menubar")
        self.menuAbrir = QtWidgets.QMenu(self.menubar)
        self.menuAbrir.setObjectName("menuAbrir")
        #Me_Voy_A_Matar.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Me_Voy_A_Matar)
        self.statusbar.setObjectName("statusbar")
        #Me_Voy_A_Matar.setStatusBar(self.statusbar)
        self.actionCargar = QtWidgets.QAction(Me_Voy_A_Matar)
        self.actionCargar.setObjectName("actionCargar")
        self.menuAbrir.addAction(self.actionCargar)
        self.menubar.addAction(self.menuAbrir.menuAction())

        self.retranslateUi(Me_Voy_A_Matar)
        QtCore.QMetaObject.connectSlotsByName(Me_Voy_A_Matar)

    def retranslateUi(self, Me_Voy_A_Matar):
        _translate = QtCore.QCoreApplication.translate
        Me_Voy_A_Matar.setWindowTitle(_translate("Me_Voy_A_Matar", "Me voy a matar"))
        self.pushButton.setText(_translate("Me_Voy_A_Matar", "Siguiente disparo"))
        self.menuAbrir.setTitle(_translate("Me_Voy_A_Matar", "Abrir"))
        self.actionCargar.setText(_translate("Me_Voy_A_Matar", "Cargar"))
        self.actionCargar.setShortcut(_translate("Me_Voy_A_Matar", "Ctrl+Q"))