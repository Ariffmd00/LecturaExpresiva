# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Ariff\Documentos\Visual Codex\Proyecto uni\proyecto lenguaje expresivo\ventanas\acercaventana.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_acercaapp(object):
    def setupUi(self, acercaapp):
        acercaapp.setObjectName("acercaapp")
        acercaapp.resize(425, 453)
        self.centralwidget = QtWidgets.QWidget(acercaapp)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background:rgb(116, 116, 116)")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setObjectName("widget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setStyleSheet("\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem1, 0, 2, 1, 1)
        self.gridLayout_3.addWidget(self.widget, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 0, 1, 1, 1)
        acercaapp.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(acercaapp)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 425, 21))
        self.menubar.setObjectName("menubar")
        self.menuAplicacion = QtWidgets.QMenu(self.menubar)
        self.menuAplicacion.setObjectName("menuAplicacion")
        self.menuRegresar = QtWidgets.QMenu(self.menubar)
        self.menuRegresar.setObjectName("menuRegresar")
        acercaapp.setMenuBar(self.menubar)
        self.actionSalir = QtWidgets.QAction(acercaapp)
        self.actionSalir.setObjectName("actionSalir")
        self.actionAcerca_de_la_app = QtWidgets.QAction(acercaapp)
        self.actionAcerca_de_la_app.setObjectName("actionAcerca_de_la_app")
        self.back = QtWidgets.QAction(acercaapp)
        self.back.setObjectName("back")
        self.menuAplicacion.addAction(self.actionSalir)
        self.menuRegresar.addAction(self.back)
        self.menubar.addAction(self.menuAplicacion.menuAction())
        self.menubar.addAction(self.menuRegresar.menuAction())

        self.retranslateUi(acercaapp)
        QtCore.QMetaObject.connectSlotsByName(acercaapp)

    def retranslateUi(self, acercaapp):
        _translate = QtCore.QCoreApplication.translate
        acercaapp.setWindowTitle(_translate("acercaapp", "MainWindow"))
        self.label.setText(_translate("acercaapp", "Programa creado y dise??ado  por:\n"
" Ra??l Ariff Moreno Dominguez\n"
" Oswaldo chi Diaz \n"
" Aldo Malrtinez Maldonado \n"
" Raul Ernesto \n"
" Alumnos del Instituto Tecnologico de Merida, \n"
" como parte de la materia de Inteligencia Artificial"))
        self.menuAplicacion.setTitle(_translate("acercaapp", "Aplicacion"))
        self.menuRegresar.setTitle(_translate("acercaapp", "Regresar"))
        self.actionSalir.setText(_translate("acercaapp", "Salir"))
        self.actionAcerca_de_la_app.setText(_translate("acercaapp", "Acerca de la app"))
        self.back.setText(_translate("acercaapp", "Inicio"))
