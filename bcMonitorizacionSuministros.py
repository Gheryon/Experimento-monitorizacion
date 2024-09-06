#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Fco José Sánchez Rodríguez
"""

#Modulo que define la base de conocimiento de la meteorología.

__docformat__ = "restructuredtext"

from esquemaConocimiento import *

class madera(Parametro):
    #clase
    def __init__(self):
        Parametro.__init__(self, nombre=u'Madera', unidad='kg')
        
        self.norma=Norma(valor=5000, valor2=3000, tipo='rango ')
        
class agua(Parametro):
    #clase
    def __init__(self):
        Parametro.__init__(self, nombre=u'Agua', unidad='litros')
        
        self.norma=Norma(valor=700000, valor2=650000, tipo='rango ')

class aceite(Parametro):
    #clase
    def __init__(self):
        Parametro.__init__(self, nombre=u'Aceite', unidad='litros')
        
        self.norma=Norma(valor=15000, valor2=10000, tipo='rango ')
        
class harina(Parametro):
    #clase
    def __init__(self):
        Parametro.__init__(self, nombre=u'Harina', unidad='kg')
        
        self.norma=Norma(valor=18000, valor2=10000, tipo='rango ')
        
class electricidad(Parametro):
    #clase
    def __init__(self):
        Parametro.__init__(self, nombre=u'Electricidad', unidad='W/dia')
        
        self.norma=Norma(valor=100000, valor2=0, tipo='<= ')

def clases():
    #Lista de parametros de la bc
    return [madera(), agua(), aceite(), harina(), electricidad()]
