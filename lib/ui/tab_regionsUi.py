# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tab_regionsUi.ui'
#
# Created: Fri Nov 29 01:58:54 2013
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_tab_regions(object):
    def setupUi(self, tab_regions):
        tab_regions.setObjectName(_fromUtf8("tab_regions"))
        tab_regions.resize(251, 448)
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
        self.page_regions_overview.setGeometry(QtCore.QRect(0, 0, 249, 404))
        self.page_regions_overview.setObjectName(_fromUtf8("page_regions_overview"))
        self.gridLayout_6 = QtGui.QGridLayout(self.page_regions_overview)
        self.gridLayout_6.setMargin(0)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.gridLayout_5 = QtGui.QGridLayout()
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setContentsMargins(-1, 0, -1, -1)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.btn_remove_shape = QtGui.QPushButton(self.page_regions_overview)
        self.btn_remove_shape.setMinimumSize(QtCore.QSize(30, 0))
        self.btn_remove_shape.setObjectName(_fromUtf8("btn_remove_shape"))
        self.gridLayout_5.addWidget(self.btn_remove_shape, 7, 1, 1, 1)
        self.tree_region_shapes = QtGui.QTreeWidget(self.page_regions_overview)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tree_region_shapes.sizePolicy().hasHeightForWidth())
        self.tree_region_shapes.setSizePolicy(sizePolicy)
        self.tree_region_shapes.setProperty("showDropIndicator", False)
        self.tree_region_shapes.setAlternatingRowColors(True)
        self.tree_region_shapes.setIndentation(0)
        self.tree_region_shapes.setObjectName(_fromUtf8("tree_region_shapes"))
        self.gridLayout_5.addWidget(self.tree_region_shapes, 5, 0, 2, 2)
        self.btn_add_shape = QtGui.QPushButton(self.page_regions_overview)
        self.btn_add_shape.setMinimumSize(QtCore.QSize(30, 0))
        self.btn_add_shape.setCheckable(True)
        self.btn_add_shape.setObjectName(_fromUtf8("btn_add_shape"))
        self.gridLayout_5.addWidget(self.btn_add_shape, 7, 0, 1, 1)
        self.gridLayout_10 = QtGui.QGridLayout()
        self.gridLayout_10.setSpacing(0)
        self.gridLayout_10.setObjectName(_fromUtf8("gridLayout_10"))
        self.table_slots = QtGui.QTableWidget(self.page_regions_overview)
        self.table_slots.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.table_slots.setAlternatingRowColors(True)
        self.table_slots.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.table_slots.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.table_slots.setShowGrid(True)
        self.table_slots.setObjectName(_fromUtf8("table_slots"))
        self.table_slots.setColumnCount(3)
        self.table_slots.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.table_slots.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.table_slots.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.table_slots.setHorizontalHeaderItem(2, item)
        self.table_slots.horizontalHeader().setMinimumSectionSize(5)
        self.table_slots.horizontalHeader().setStretchLastSection(True)
        self.table_slots.verticalHeader().setVisible(False)
        self.gridLayout_10.addWidget(self.table_slots, 1, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_10, 8, 0, 1, 2)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setContentsMargins(3, 0, -1, -1)
        self.gridLayout_3.setHorizontalSpacing(1)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.spin_shape_x = QtGui.QSpinBox(self.page_regions_overview)
        self.spin_shape_x.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spin_shape_x.setButtonSymbols(QtGui.QAbstractSpinBox.PlusMinus)
        self.spin_shape_x.setAccelerated(True)
        self.spin_shape_x.setMinimum(-2048)
        self.spin_shape_x.setMaximum(2048)
        self.spin_shape_x.setObjectName(_fromUtf8("spin_shape_x"))
        self.gridLayout_3.addWidget(self.spin_shape_x, 0, 5, 1, 1)
        self.lbl_y = QtGui.QLabel(self.page_regions_overview)
        self.lbl_y.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_y.setMargin(2)
        self.lbl_y.setObjectName(_fromUtf8("lbl_y"))
        self.gridLayout_3.addWidget(self.lbl_y, 0, 2, 1, 1)
        self.lbl_x = QtGui.QLabel(self.page_regions_overview)
        self.lbl_x.setMargin(2)
        self.lbl_x.setObjectName(_fromUtf8("lbl_x"))
        self.gridLayout_3.addWidget(self.lbl_x, 0, 4, 1, 1)
        self.ckb_trigger = QtGui.QCheckBox(self.page_regions_overview)
        self.ckb_trigger.setChecked(True)
        self.ckb_trigger.setObjectName(_fromUtf8("ckb_trigger"))
        self.gridLayout_3.addWidget(self.ckb_trigger, 0, 0, 1, 1)
        self.lbl_color = QtGui.QLabel(self.page_regions_overview)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_color.sizePolicy().hasHeightForWidth())
        self.lbl_color.setSizePolicy(sizePolicy)
        self.lbl_color.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.lbl_color.setFrameShape(QtGui.QFrame.Box)
        self.lbl_color.setText(_fromUtf8(""))
        self.lbl_color.setMargin(0)
        self.lbl_color.setObjectName(_fromUtf8("lbl_color"))
        self.gridLayout_3.addWidget(self.lbl_color, 0, 1, 1, 1)
        self.spin_shape_y = QtGui.QSpinBox(self.page_regions_overview)
        self.spin_shape_y.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spin_shape_y.setButtonSymbols(QtGui.QAbstractSpinBox.PlusMinus)
        self.spin_shape_y.setAccelerated(True)
        self.spin_shape_y.setMinimum(-2048)
        self.spin_shape_y.setMaximum(2048)
        self.spin_shape_y.setObjectName(_fromUtf8("spin_shape_y"))
        self.gridLayout_3.addWidget(self.spin_shape_y, 0, 3, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_3, 0, 0, 1, 2)
        self.gridLayout_6.addLayout(self.gridLayout_5, 0, 0, 1, 1)
        self.toolBox.addItem(self.page_regions_overview, _fromUtf8(""))
        self.page_regions_IO = QtGui.QWidget()
        self.page_regions_IO.setGeometry(QtCore.QRect(0, 0, 249, 404))
        self.page_regions_IO.setObjectName(_fromUtf8("page_regions_IO"))
        self.gridLayout_7 = QtGui.QGridLayout(self.page_regions_IO)
        self.gridLayout_7.setMargin(0)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.gridLayout_9 = QtGui.QGridLayout()
        self.gridLayout_9.setObjectName(_fromUtf8("gridLayout_9"))
        self.combo_label = QtGui.QComboBox(self.page_regions_IO)
        self.combo_label.setEnabled(False)
        self.combo_label.setEditable(True)
        self.combo_label.setObjectName(_fromUtf8("combo_label"))
        self.gridLayout_9.addWidget(self.combo_label, 0, 1, 1, 2)
        self.pushButton_15 = QtGui.QPushButton(self.page_regions_IO)
        self.pushButton_15.setEnabled(False)
        self.pushButton_15.setObjectName(_fromUtf8("pushButton_15"))
        self.gridLayout_9.addWidget(self.pushButton_15, 1, 1, 1, 1)
        self.pushButton_14 = QtGui.QPushButton(self.page_regions_IO)
        self.pushButton_14.setEnabled(False)
        self.pushButton_14.setObjectName(_fromUtf8("pushButton_14"))
        self.gridLayout_9.addWidget(self.pushButton_14, 2, 1, 1, 1)
        self.pushButton_13 = QtGui.QPushButton(self.page_regions_IO)
        self.pushButton_13.setEnabled(False)
        self.pushButton_13.setObjectName(_fromUtf8("pushButton_13"))
        self.gridLayout_9.addWidget(self.pushButton_13, 2, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_9.addItem(spacerItem, 3, 1, 2, 2)
        self.pushButton_12 = QtGui.QPushButton(self.page_regions_IO)
        self.pushButton_12.setEnabled(False)
        self.pushButton_12.setObjectName(_fromUtf8("pushButton_12"))
        self.gridLayout_9.addWidget(self.pushButton_12, 1, 2, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_9, 0, 2, 1, 1)
        self.toolBox.addItem(self.page_regions_IO, _fromUtf8(""))
        self.gridLayout_2.addWidget(self.toolBox, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        self.retranslateUi(tab_regions)
        self.toolBox.setCurrentIndex(0)
        self.toolBox.layout().setSpacing(0)
        QtCore.QMetaObject.connectSlotsByName(tab_regions)

    def retranslateUi(self, tab_regions):
        tab_regions.setWindowTitle(_translate("tab_regions", "Form", None))
        self.btn_remove_shape.setText(_translate("tab_regions", "&Remove", None))
        self.tree_region_shapes.headerItem().setText(0, _translate("tab_regions", "Shapes", None))
        self.btn_add_shape.setStatusTip(_translate("tab_regions", "Drag: Rectangle. Shift+drag: Circle. Ctrl+drag: Line.", None))
        self.btn_add_shape.setText(_translate("tab_regions", "&Add", None))
        item = self.table_slots.horizontalHeaderItem(0)
        item.setText(_translate("tab_regions", "Collision", None))
        item = self.table_slots.horizontalHeaderItem(1)
        item.setText(_translate("tab_regions", "Pin", None))
        item = self.table_slots.horizontalHeaderItem(2)
        item.setText(_translate("tab_regions", "Logic", None))
        self.lbl_y.setText(_translate("tab_regions", "y:", None))
        self.lbl_x.setText(_translate("tab_regions", "x:", None))
        self.ckb_trigger.setText(_translate("tab_regions", "Trigger", None))
        self.lbl_color.setToolTip(_translate("tab_regions", "Click me to change...", None))
        self.lbl_color.setStatusTip(_translate("tab_regions", "Click me to change...", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_regions_overview), _translate("tab_regions", "Shapes", None))
        self.pushButton_15.setText(_translate("tab_regions", "Open", None))
        self.pushButton_14.setText(_translate("tab_regions", "Clone", None))
        self.pushButton_13.setText(_translate("tab_regions", "Delete", None))
        self.pushButton_12.setText(_translate("tab_regions", "Save", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_regions_IO), _translate("tab_regions", "In/Out", None))

