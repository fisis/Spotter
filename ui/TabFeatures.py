# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 14:19:24 2013
@author: <Ronny Eichler> ronny.eichler@gmail.com


"""

import sys
from PyQt4 import QtGui, QtCore

sys.path.append('./ui')
from tab_featuresUi import Ui_tab_features

tab_type = "newLED"

class Tab(QtGui.QWidget, Ui_tab_features):
    
    name = None
    feature = None
    
    def __init__(self, parent, feature_handle, label = None):
        if label == None:
            self.name = tab_type
        else:
            self.name = tab_type
        super(QtGui.QWidget, self).__init__(parent)
        self.setupUi(self)

    def update(self):
        self.combo_label.setEditText(self.name)