# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tab_regionsUi.ui'
#
# Created: Mon Jan 14 23:57:57 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_tab_regions(object):
    def setupUi(self, tab_regions):
        tab_regions.setObjectName(_fromUtf8("tab_regions"))
        tab_regions.resize(241, 325)
        self.gridLayout = QtGui.QGridLayout(tab_regions)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setSpacing(1)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.toolBox = QtGui.QToolBox(tab_regions)
        self.toolBox.setFrameShape(QtGui.QFrame.NoFrame)
        self.toolBox.setFrameShadow(QtGui.QFrame.Plain)
        self.toolBox.setLineWidth(0)
        self.toolBox.setObjectName(_fromUtf8("toolBox"))
        self.page_regions_overview = QtGui.QWidget()
        self.page_regions_overview.setGeometry(QtCore.QRect(0, 0, 239, 248))
        self.page_regions_overview.setObjectName(_fromUtf8("page_regions_overview"))
        self.gridLayout_6 = QtGui.QGridLayout(self.page_regions_overview)
        self.gridLayout_6.setMargin(0)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.gridLayout_5 = QtGui.QGridLayout()
        self.gridLayout_5.setSpacing(1)
        self.gridLayout_5.setContentsMargins(-1, 0, -1, -1)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.combo_Object = QtGui.QComboBox(self.page_regions_overview)
        self.combo_Object.setEditable(False)
        self.combo_Object.setObjectName(_fromUtf8("combo_Object"))
        self.gridLayout_5.addWidget(self.combo_Object, 1, 0, 1, 3)
        self.ckb_trigger = QtGui.QCheckBox(self.page_regions_overview)
        self.ckb_trigger.setChecked(True)
        self.ckb_trigger.setObjectName(_fromUtf8("ckb_trigger"))
        self.gridLayout_5.addWidget(self.ckb_trigger, 0, 0, 1, 1)
        self.treeWidget = QtGui.QTreeWidget(self.page_regions_overview)
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        self.gridLayout_5.addWidget(self.treeWidget, 2, 0, 1, 3)
        self.btn_select_region = QtGui.QPushButton(self.page_regions_overview)
        self.btn_select_region.setCheckable(True)
        self.btn_select_region.setObjectName(_fromUtf8("btn_select_region"))
        self.gridLayout_5.addWidget(self.btn_select_region, 0, 1, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_5, 0, 1, 1, 1)
        self.toolBox.addItem(self.page_regions_overview, _fromUtf8(""))
        self.page_regions_conditions = QtGui.QWidget()
        self.page_regions_conditions.setGeometry(QtCore.QRect(0, 0, 239, 248))
        self.page_regions_conditions.setObjectName(_fromUtf8("page_regions_conditions"))
        self.gridLayout_8 = QtGui.QGridLayout(self.page_regions_conditions)
        self.gridLayout_8.setMargin(0)
        self.gridLayout_8.setSpacing(0)
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.toolBox.addItem(self.page_regions_conditions, _fromUtf8(""))
        self.page_regions_IO = QtGui.QWidget()
        self.page_regions_IO.setGeometry(QtCore.QRect(0, 0, 239, 248))
        self.page_regions_IO.setObjectName(_fromUtf8("page_regions_IO"))
        self.gridLayout_7 = QtGui.QGridLayout(self.page_regions_IO)
        self.gridLayout_7.setMargin(0)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.pushButton_8 = QtGui.QPushButton(self.page_regions_IO)
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.gridLayout_7.addWidget(self.pushButton_8, 2, 3, 1, 1)
        self.pushButton_9 = QtGui.QPushButton(self.page_regions_IO)
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
        self.gridLayout_7.addWidget(self.pushButton_9, 2, 1, 1, 1)
        self.pushButton_4 = QtGui.QPushButton(self.page_regions_IO)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.gridLayout_7.addWidget(self.pushButton_4, 1, 1, 1, 1)
        self.pushButton_5 = QtGui.QPushButton(self.page_regions_IO)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.gridLayout_7.addWidget(self.pushButton_5, 1, 3, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem, 0, 1, 1, 1)
        self.toolBox.addItem(self.page_regions_IO, _fromUtf8(""))
        self.gridLayout_2.addWidget(self.toolBox, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        self.retranslateUi(tab_regions)
        self.toolBox.setCurrentIndex(0)
        self.toolBox.layout().setSpacing(0)
        QtCore.QMetaObject.connectSlotsByName(tab_regions)

    def retranslateUi(self, tab_regions):
        tab_regions.setWindowTitle(QtGui.QApplication.translate("tab_regions", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.ckb_trigger.setText(QtGui.QApplication.translate("tab_regions", "Trigger", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(0, QtGui.QApplication.translate("tab_regions", "ROIs", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_select_region.setText(QtGui.QApplication.translate("tab_regions", "Select Region", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_regions_overview), QtGui.QApplication.translate("tab_regions", "Tracking", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_regions_conditions), QtGui.QApplication.translate("tab_regions", "Conditions/Triggers", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_8.setText(QtGui.QApplication.translate("tab_regions", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_9.setText(QtGui.QApplication.translate("tab_regions", "Open", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_4.setText(QtGui.QApplication.translate("tab_regions", "Clone", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_5.setText(QtGui.QApplication.translate("tab_regions", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_regions_IO), QtGui.QApplication.translate("tab_regions", "In/Out", None, QtGui.QApplication.UnicodeUTF8))

