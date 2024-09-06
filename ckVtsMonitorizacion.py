#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Fco José Sánchez Rodríguez
"""

import sys
from PyQt4 import QtCore
from PyQt4 import QtGui
from PyQt4.QtCore import pyqtSlot, SIGNAL, SLOT

import ckCtrlMonitorizacion as ctrl
import bcMonitorizacionBatallas as bcBat
import bcMonitorizacionSuministros as bcSum
import bcMonitorizacionContaminacion as bcCon
import ckModMonitorizacion as mod

class MonitorizacionDlg(QtGui.QWidget):
    """
    Clase encargada de la interfaz de la aplicación de monitorización
    """
    def __init__(self):
        super(MonitorizacionDlg, self).__init__()
        self.dominio='Batallas'
        self.crearTablasDescripcionDominio()
        
        labelComboBoxDominio=QtGui.QLabel("Dominio", self)
        self.comboBoxDominio= QtGui.QComboBox()
        self.comboBoxDominio.addItem('Batallas')
        self.comboBoxDominio.addItem('Suministros')
        self.comboBoxDominio.addItem('Contaminacion')
        
        self.comboBoxDominio.activated[str].connect(self.dominioModificado)
        
        labelTextjustificacionL=QtGui.QLabel(u"Justificación de la monitorización",self)
        self.plainTextEditExplicacion = QtGui.QPlainTextEdit()
        self.plainTextEditExplicacion.setReadOnly(True)

        labelTextDescripcionDominio=QtGui.QLabel(u"Descripción del dominio",self)

        labelComboBoxSemana=QtGui.QLabel("Semana", self)
        self.comboBoxSemana = QtGui.QComboBox()

        indices=["1","2","3","4","5","6","7","8","9","10"]

        for indice in indices:
            self.comboBoxSemana.addItem(indice)

        self.monitorizarButtom=QtGui.QPushButton('Monitorizar')
        self.borrarButtom=QtGui.QPushButton('Borrar')
        self.salirButtom=QtGui.QPushButton('Salir')

        self.grid = QtGui.QGridLayout()
        self.grid.setSpacing(15)

        self.grid.addWidget(labelTextjustificacionL,2,2)
        self.grid.addWidget(self.plainTextEditExplicacion, 3,2,1,2)

        self.grid.addWidget(labelTextDescripcionDominio,2,5)
        self.grid.addWidget(self.tablaWidgetSuministros,3,5,1,4)
        self.tablaWidgetSuministros.hide()
        self.grid.addWidget(self.tablaWidgetContaminacion,3,5,1,4)
        self.tablaWidgetContaminacion.hide()
        self.grid.addWidget(self.tablaWidgetBatallas,3,5,1,4)

        self.grid.addWidget(labelComboBoxDominio,4,5)
        self.grid.addWidget(self.comboBoxDominio,5,5,1,4)

        self.grid.addWidget(labelComboBoxSemana,6,5)
        self.grid.addWidget(self.comboBoxSemana,7,5,1,4)

        self.grid.addWidget(self.monitorizarButtom,4,2)
        self.grid.addWidget(self.borrarButtom,4,3)
        self.grid.addWidget(self.salirButtom,5,2)

        self.setLayout(self.grid)

        self.setGeometry(300, 200, 675, 400)
        self.setWindowTitle("Tarea de monitorizacion")
        self.center()
        self.show()

        self.monitorizarButtom.clicked.connect(self.monitorizar)
        self.comboBoxSemana.activated[str].connect(semana)

        self.monitorizarButtom.setShortcut('Ctrl+M')
        self.borrarButtom.clicked.connect(self.plainTextEditExplicacion.clear)
        self.borrarButtom.setShortcut('Ctrl+D')
        self.salirButtom.clicked.connect(self.close)
        self.salirButtom.setShortcut('Ctrl+Q')

    def center(self):
        """
        Metodo para centrar la ventana en la pantalla
        """
        frameGm = self.frameGeometry()
        screen = QtGui.QApplication.desktop().screenNumber(QtGui.QApplication.desktop().cursor().pos())
        centerPoint = QtGui.QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())

    def crearTablasDescripcionDominio(self):
        """
        Metodo encargado de crear un tabla representativa de cada dominio
        a traves de cual se podran indicar la descripción del mismo
        """
        self.etiquetasHeader= ['PARAMETRO', 'NORMA', 'UNIDAD']

        #Batallas
        self.clasesBC=bcBat.clases()

        # Crear la tabla relativa al dominio de batallas#
        self.tablaWidgetBatallas= QtGui.QTableWidget(len(self.clasesBC), 3)
        self.tablaWidgetBatallas.setColumnWidth(0,120)
        self.tablaWidgetBatallas.setColumnWidth(1,130)
        self.tablaWidgetBatallas.setColumnWidth(2,110)
        self.tablaWidgetBatallas.setHorizontalHeaderLabels(self.etiquetasHeader)

        i=0
        for c in self.clasesBC:
            parametro = QtGui.QTableWidgetItem(c.nombre)
            parametro.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)

            if int(c.norma.valor2) == 0:
    				norma = QtGui.QTableWidgetItem(c.norma.tipo + ' ' + str(c.norma.valor))
            else:
                norma = QtGui.QTableWidgetItem(c.norma.tipo + ' ' + str(c.norma.valor2)+ ' - ' + str(c.norma.valor))

            norma.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)

            unidad = QtGui.QTableWidgetItem(c.unidad)
            unidad.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)

            self.tablaWidgetBatallas.setItem(i,0,parametro)
            self.tablaWidgetBatallas.setItem(i,1,norma)
            self.tablaWidgetBatallas.setItem(i,2,unidad)
            i=i+1
            
        #Suministros
        self.clasesBC=bcSum.clases()

        #Creación de la tabla relativa al dominio de los suministros
        self.tablaWidgetSuministros = QtGui.QTableWidget(len(self.clasesBC), 3)
        self.tablaWidgetSuministros.setColumnWidth(0,120)
        self.tablaWidgetSuministros.setColumnWidth(1,130)
        self.tablaWidgetSuministros.setColumnWidth(2,110)
        self.tablaWidgetSuministros.setHorizontalHeaderLabels(self.etiquetasHeader)

        i=0
        for c in self.clasesBC:
            parametro = QtGui.QTableWidgetItem(c.nombre)
            parametro.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)

            if int(c.norma.valor2) == 0:
    				norma = QtGui.QTableWidgetItem(c.norma.tipo + ' ' + str(c.norma.valor))
            else:
                norma = QtGui.QTableWidgetItem(c.norma.tipo + ' ' + str(c.norma.valor2)+ ' - ' + str(c.norma.valor))

            norma.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)

            unidad = QtGui.QTableWidgetItem(c.unidad)
            unidad.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)

            self.tablaWidgetSuministros.setItem(i,0,parametro)
            self.tablaWidgetSuministros.setItem(i,1,norma)
            self.tablaWidgetSuministros.setItem(i,2,unidad)
            i=i+1
            
        #Contaminacion
        self.clasesBC=bcCon.clases()

        #Creación de la tabla relativa al dominio de contaminacion
        self.tablaWidgetContaminacion = QtGui.QTableWidget(len(self.clasesBC), 3)
        self.tablaWidgetContaminacion.setColumnWidth(0,130)
        self.tablaWidgetContaminacion.setColumnWidth(1,120)
        self.tablaWidgetContaminacion.setColumnWidth(2,110)
        self.tablaWidgetContaminacion.setHorizontalHeaderLabels(self.etiquetasHeader)

        i=0
        for c in self.clasesBC:
            parametro = QtGui.QTableWidgetItem(c.nombre)
            parametro.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)

            if int(c.norma.valor2) == 0:
    				norma = QtGui.QTableWidgetItem(c.norma.tipo + ' ' + str(c.norma.valor))
            else:
                norma = QtGui.QTableWidgetItem(c.norma.tipo + ' ' + str(c.norma.valor2)+ ' - ' + str(c.norma.valor))

            norma.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)

            unidad = QtGui.QTableWidgetItem(c.unidad)
            unidad.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)

            self.tablaWidgetContaminacion.setItem(i,0,parametro)
            self.tablaWidgetContaminacion.setItem(i,1,norma)
            self.tablaWidgetContaminacion.setItem(i,2,unidad)
            i=i+1

    def dominioModificado(self, text):
        """
        Metodo que modifica y ajusta la interfaz de usuario dependiendo del
        dominio seleccionado
        """

        #Comprobar que el dominio seleccionado sea distinto al actual
        if self.dominio != text:
    			#Se actualiza el dominio por el seleccionado
            self.dominio = text

    			#Actualizar la tabla descriptiva del objeto a clasisficar
            if self.dominio == "Batallas":
                self.tablaWidgetSuministros.hide()
                self.tablaWidgetBatallas.show()
                self.tablaWidgetContaminacion.hide()

            elif self.dominio == "Suministros":
                self.tablaWidgetBatallas.hide()
                self.tablaWidgetSuministros.show()
                self.tablaWidgetContaminacion.hide()
                
            elif self.dominio == "Contaminacion":
                self.tablaWidgetBatallas.hide()
                self.tablaWidgetSuministros.hide()
                self.tablaWidgetContaminacion.show()

            self.plainTextEditExplicacion.clear()


    def monitorizar(self):
        """
        Metodo encargado de iniciar el proceso de monitorizacion
        """
        explicacion = ctrl.eventoMonitorizar(self.dominio)

        self.plainTextEditExplicacion.clear()
        self.plainTextEditExplicacion.appendPlainText(explicacion)
        self.plainTextEditExplicacion.moveCursor(QtGui.QTextCursor.Start)
 
        
class semana():
	diaSemana = 1
	print diaSemana
    
	def execute():
		return diaSemana

if __name__=='__main__':
    app = QtGui.QApplication(sys.argv)
    form = MonitorizacionDlg()
    sys.exit(app.exec_())
