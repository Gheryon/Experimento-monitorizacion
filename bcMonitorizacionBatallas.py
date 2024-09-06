#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Modulo que define la base de conocimiento de las batallas.

__docformat__ = "restructuredtext"

from esquemaConocimiento import *

class infanteriaIni(Parametro):
    #clase
    def __init__(self):
        Parametro.__init__(self, nombre=u'Infanteria inicial', unidad='soldados')
        
        self.norma=Norma(valor=30000, valor2=15000, tipo='rango ')
        
class infanteriaFin(Parametro):
    #clase
    def __init__(self):
        Parametro.__init__(self, nombre=u'Infanteria final', unidad='soldados')
        
        self.norma=Norma(valor=20000, valor2=15000, tipo='rango ')

class caballeriaIni(Parametro):
    #clase
    def __init__(self):
        Parametro.__init__(self, nombre=u'Caballeria inicial', unidad='soldados')
        
        self.norma=Norma(valor=10000, valor2=5000, tipo='rango ')
        
class caballeriaFin(Parametro):
    #clase
    def __init__(self):
        Parametro.__init__(self, nombre=u'Caballeria final', unidad='soldados')
        
        self.norma=Norma(valor=5000, valor2=4000, tipo='rango ')
        
class cannons(Parametro):
    #clase
    def __init__(self):
        Parametro.__init__(self, nombre=u'Cannons', unidad=u'cannons')
        
        self.norma=Norma(valor=30, valor2=10, tipo='rango ')

def clases():
    #Lista de parametros de la bc
    return [infanteriaIni(), infanteriaFin(), caballeriaIni(), caballeriaFin(), cannons()]
