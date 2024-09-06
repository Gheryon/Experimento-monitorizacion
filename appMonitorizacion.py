#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Fco José Sánchez Rodríguez
"""

import sys
from PyQt4 import QtGui
import ckVtsMonitorizacion

app = QtGui.QApplication(sys.argv)
form = ckVtsMonitorizacion.MonitorizacionDlg()
sys.exit(app.exec_())
