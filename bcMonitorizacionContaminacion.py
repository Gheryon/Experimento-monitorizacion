#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Fco José Sánchez Rodríguez
"""

#Modulo que define la base de conocimiento de la contaminación.

__docformat__ = "restructuredtext"

from esquemaConocimiento import *

class dioxidoCarbono(Parametro):
    #clase
    def __init__(self):
        Parametro.__init__(self, nombre=u'Dioxido de carbono', unidad='ppm')
        
        self.norma=Norma(valor=280, valor2=0, tipo='>= ')

class monoxidoCarbono(Parametro):
    #clase
    def __init__(self):
        Parametro.__init__(self, nombre=u'Monoxido de carbono', unidad='ppm')
        
        self.norma=Norma(valor=55, valor2=0, tipo='>= ')
        
class plasticos(Parametro):
    #clase
    def __init__(self):
        Parametro.__init__(self, nombre=u'Plasticos', unidad='toneladas')
        
        self.norma=Norma(valor=70000, valor2=0, tipo='>= ')
        
class petroleo(Parametro):
    #clase
    def __init__(self):
        Parametro.__init__(self, nombre=u'Petroleo', unidad='barriles')
        
        self.norma=Norma(valor=18000, valor2=10000, tipo='rango ')
        
class radiacion(Parametro):
    #clase
    def __init__(self):
        Parametro.__init__(self, nombre=u'Radiacion', unidad='mili Sievert')
        
        self.norma=Norma(valor=250, valor2=0, tipo='<= ')

def clases():
    #Lista de parametros de la bc
    return [dioxidoCarbono(), monoxidoCarbono(), plasticos(), petroleo(), radiacion()]

