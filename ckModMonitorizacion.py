#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Fco Jose Sanchez Rodriguez
"""

__docformat__ = "restructuredtext"

import os
import datetime
import random

from esquemaConocimiento import *
import bcMonitorizacionBatallas as bcBats
import bcMonitorizacionSuministros as bcSum
import bcMonitorizacionContaminacion as bcCon

class MetodoMonitorizacion():
    """
    Clase encargada de implementar el metodo y las funciones necesarias para la 
    tarea de monitorización
    """
    def __init__(self, dominio):
        self.dominio = dominio
        self.parametrosCandidatos=[]
        self.explicacion=u''
    
    def execute(self):
        """
        Metodo que realiza la monitorizacion
        """
        #Se encuentra un hallazgo
        recibir = Recibir(self.dominio)
        self.parametrosCandidatos, self.hallazgo = recibir.execute()
        self.explicacion+=u'\nHallazgo encontrado: ' + str(self.hallazgo.valor) + '\n\n'

        # Comienza la ejecución
        seleccionar = Seleccionar(self.parametrosCandidatos, self.hallazgo)
        self.parametro = seleccionar.execute()
        self.explicacion+=u'Se selecciona el parametro: ' + self.parametro.nombre + '\n\n'

        especificar = Especificar(self.parametro)
        self.norma = especificar.execute()
        if int(self.norma.valor2) == 0:
            self.explicacion+=u'Se especifica la norma: ' + self.norma.tipo + ' ' + str(self.norma.valor) + '\n\n'
        else:
            self.explicacion+=u'Se especifica la norma: ' + self.norma.tipo + ' ' + str(self.norma.valor2) + ' - ' + str(self.norma.valor) + '\n\n'

        comparar = Comparar(self.hallazgo, self.norma)
        resultado, self.diferencia = comparar.execute()
        self.explicacion+=u'Se compara el hallazgo con la norma y se obtiene la diferencia: ' + str(self.diferencia) +  '\n\n'
        if resultado:
            self.explicacion+=u'\nNo hay discrepancia, todo normal.\n'
        else:
            self.explicacion+=u'\n¡Importante! El hallazgo no se corresponde con la norma, hay una discrepancia\n'
        
        self.guardar(self.explicacion)
        return self.explicacion
    
    def guardar(self, datos):
        """
        Funcion para guardar los datos de distintas monitorizaciones en un fichero
        historico
        """
        hora_actual = str(datetime.datetime.now())

        if self.dominio=='Batallas':
            nombreFichero = "DatosHistoricosBatallas.txt"
            parametrosCandidatos = bcBats.clases()
        elif self.dominio=='Suministros':
            nombreFichero = "DatosHistoricosSuministros.txt"
            parametrosCandidatos = bcSum.clases()
        elif self.dominio=='Contaminacion':
            nombreFichero = "DatosHistoricosContaminacion.txt"
            parametrosCandidatos = bcCon.clases()
        DH = DatosHistoricos(nombreFichero)
        fechaInicio = DH.fechaInicio()

        """
        Apertura y escritura en el fichero
        """
        fichero = open(nombreFichero, 'a')
        if os.stat(nombreFichero).st_size == 0:
            fichero.write("Fecha de inicio de la monitorización: ")
            fichero.write(fechaInicio)
            fichero.write("\n")
            fichero.write("-------------------------------------------------------\n")

        fichero.write("Fecha de fin de la monitorización de datos: ")
        fichero.write(hora_actual)
        fichero.write("\n")
        fichero.write(datos.encode('utf-8'))
        fichero.write("\n")
        fichero.write("-------------------------------------------------------\n")

        fichero.close()
        
class Inferencia():
    #Clase de las inferencias
    def __init__(self):
        pass
    def execute(self):
        pass

class FuncionTransferencia():
    #Clase de la función de transferencia
    def __init__(self):
        pass
    def execute(self):
        pass

class Recibir(FuncionTransferencia):
    """
    Función que se encarga de recibir la información guardada en los ficheros
    relacionados con cada dominio respectivamente
    """
    def __init__(self, dominio):
        FuncionTransferencia.__init__(self)
        self.dominio = dominio

    def execute(self):
        if self.dominio=='Batallas':
            nombreFichero = "batallas.txt"
            parametrosCandidatos = bcBats.clases()
        elif self.dominio=='Suministros':
            nombreFichero = "suministros.txt"
            parametrosCandidatos = bcSum.clases()
        elif self.dominio=='Contaminacion':
            nombreFichero = "contaminacion.txt"
            parametrosCandidatos = bcCon.clases()
        diccionario = {}

        """
        Apertura y lectura del fichero
        """
        fichero = open(nombreFichero, 'r')
        for linea in fichero:
            """
            Se separa el nombre de los parámetros con : y se añaden a una lista
            separados por ,
            """
            parametro = linea.split(":")
            datos = parametro[1].split(",")
            datos.remove('\n') 
            #Los añadimos a un diccionario donde estarán todos los datos existentes
            diccionario[parametro[0]] = datos

        fichero.close()

        #Se monitoriza aleatoriamente uno de los parámetros.
        parametro = random.choice(diccionario.keys())
        valor = random.choice(diccionario[parametro])
        hallazgo = Hallazgo(parametro, valor)
        return parametrosCandidatos, hallazgo

class Seleccionar(Inferencia):
    """
    Metodo que selecciona un parametro para monitorizar
    """
    def __init__(self, parametrosCandidatos, hallazgo):
        #Constructor de clase
        Inferencia.__init__(self)
        self.hallazgo = hallazgo
        self.parametrosCandidatos = parametrosCandidatos

    def execute(self):
        #Se encargar de ejecutar Seleccionar
        for parametro in self.parametrosCandidatos:
            if parametro.nombre == self.hallazgo.parametro:
                return parametro

class Especificar(Inferencia):
    """
    Metodo que devuelve la norma relacionada con el parámetro seleccionado
    """
    def __init__(self, parametro):
        #Parámetro que se monitoriza
        Inferencia.__init__(self)
        self.parametro = parametro

    def execute(self):
        return self.parametro.norma

class Comparar(Inferencia):
    """
    Metodo que ompara el hallazgo realizado con la norma esperada
    """
    def __init__(self, hallazgo, norma):
		#Constructor
		Inferencia.__init__(self)
		self.hallazgo = hallazgo
		self.norma = norma
		self.explicacion= u''

    def execute(self):
        """
        Metodo encargado de realizar la comparacion del hallazgo con la norma
        para encontrar discrepancias. Para ello se utilizan las normas:
        - rango
        - <=
        - >=
        """

        dif = Diferencia(int(self.hallazgo.valor), int(self.norma.valor))
        self.diferencia = dif.diferencia()

        if int(self.hallazgo.valor) >= int(self.norma.valor2) and int(self.hallazgo.valor) <= int(self.norma.valor):
            diferenciaT = True
        else:
            diferenciaT = False

        if self.norma.tipo == 'rango ':
            if diferenciaT:
                return True, "Dentro del rango"
            else:
                return False, abs(self.diferencia)
                Discrepancia(abs(self.diferencia))
        
        if self.norma.tipo == '<=':
            if int(self.hallazgo.valor) <= int(self.norma.valor):
                return True, abs(self.diferencia)
            else:
                return False, abs(self.diferencia)
                Discrepancia(abs(self.diferencia))
        
        if self.norma.tipo == '>=':
            if int(self.hallazgo.valor) >= int(self.norma.valor):
                return True, abs(self.diferencia)
            else:
                return False, abs(self.diferencia)
                Discrepancia(abs(self.diferencia))