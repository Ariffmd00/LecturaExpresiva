# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Ariff\Documentos\Visual Codex\Proyecto uni\proyecto lenguaje expresivo\ventanas\explicacionLEventana.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_acercaapp(object):
    def setupUi(self, acercaapp):
        acercaapp.setObjectName("acercaapp")
        acercaapp.resize(670, 453)
        self.centralwidget = QtWidgets.QWidget(acercaapp)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background:rgb(116, 116, 116)")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(self.widget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setStyleSheet("font: 63 24pt \"Lucida Sans\";")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addWidget(self.frame_2)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setStyleSheet("\n"
"font: 63 12pt \"Lucida Sans\";")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.verticalLayout_2.addWidget(self.widget)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.btncontinuar = QtWidgets.QPushButton(self.frame_3)
        self.btncontinuar.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.btncontinuar.setObjectName("btncontinuar")
        self.horizontalLayout_2.addWidget(self.btncontinuar)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.gridLayout_2.addWidget(self.frame, 0, 1, 1, 1)
        acercaapp.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(acercaapp)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 670, 21))
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
        self.label_3.setText(_translate("acercaapp", "Para iniciar es importante\n"
"saber sobre la lectura expresiva:"))
        self.label.setText(_translate("acercaapp", "La lectura expresiva es una pr??ctica en la que un lector trata de expresar\n"
" las ideas y  emociones inmersas en un texto para que lleguen a ser \n"
"captadas por los oyentes."))
        self.btncontinuar.setText(_translate("acercaapp", "Continuar"))
        self.menuAplicacion.setTitle(_translate("acercaapp", "Aplicacion"))
        self.menuRegresar.setTitle(_translate("acercaapp", "Regresar"))
        self.actionSalir.setText(_translate("acercaapp", "Salir"))
        self.actionAcerca_de_la_app.setText(_translate("acercaapp", "Acerca de la app"))
        self.back.setText(_translate("acercaapp", "Inicio"))
