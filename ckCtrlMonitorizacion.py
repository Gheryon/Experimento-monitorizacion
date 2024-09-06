#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Fco José Sánchez Rodríguez
"""

__docformat__ = "restructuredtext"

from PyQt4 import QtGui
import ckModMonitorizacion as modelo

def eventoMonitorizar(dominio):
	#Metodo para ejecutar la monitorizacion

	mod = modelo.MetodoMonitorizacion(dominio)
	return mod.execute()
