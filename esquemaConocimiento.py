#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Fco José Sánchez Rodríguez
"""

#Fichero que define las partes fundamentales de la base de conocimiento: parametro, hallazgo y norma
__docformat__ = "restructuredtext"

import types
import datetime

class Parametro():
	"""
    Representa un dato relevante para monitorizar
   """
	def __init__(self, nombre, unidad):
		self.nombre=nombre
		self.unidad=unidad

class Norma():
    """
    Representa el valor esperado con un correcto funcionamiento   
    """
    def __init__(self, valor, valor2, tipo):
        self.valor=valor
        self.valor2=valor2
        self.tipo=tipo

class Discrepancia():
    """
    Representa la discrepancia de la diferencia con la norma 
    """
    def __init__(self,valor):
        self.discrepancia #Puede ser true o false

class Hallazgo():
    """
    Representa los hallazgos recibidos
    """
    def __init__(self, parametro, valor):
        self.parametro=parametro
        self.valor=valor

class Diferencia():
    """
    Representa la diferencia entre dos valores
    """
    def __init__(self,valor1,valor2):
    	self.hallazgo=valor1
    	self.norma=valor2
    def diferencia(self):
		self.diferencia=self.hallazgo-self.norma
		return self.diferencia

class DatosHistoricos():
	def __init__(self,nombreF):
		self.nombreFichero = nombreF
		self.fechaInit = ""
	def fechaInicio(self):
		if len(self.fechaInit) < 1:
			self.fechaInit = str(datetime.datetime.now())
			return self.fechaInit


if __name__=='__main__':
    print 'prueba'
    