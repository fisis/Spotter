# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tab_regionsUi.ui'
#
# Created: Sun Feb 17 16:51:11 2013
#      by: PyQt4 UI code generator 4.9.5
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
        tab_regions.resize(241, 324)
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
        self.page_regions_overview.setGeometry(QtCore.QRect(0, 0, 239, 259))
        self.page_regions_overview.setObjectName(_fromUtf8("page_regions_overview"))
        self.gridLayout_6 = QtGui.QGridLayout(self.page_regions_overview)
        self.gridLayout_6.setMargin(0)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.gridLayout_5 = QtGui.QGridLayout()
        self.gridLayout_5.setSpacing(1)
        self.gridLayout_5.setContentsMargins(-1, 0, -1, -1)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.btn_add_shape = QtGui.QPushButton(self.page_regions_overview)
        self.btn_add_shape.setMinimumSize(QtCore.QSize(30, 0))
        self.btn_add_shape.setCheckable(True)
        self.btn_add_shape.setObjectName(_fromUtf8("btn_add_shape"))
        self.gridLayout_5.addWidget(self.btn_add_shape, 8, 0, 1, 1)
        self.btn_remove_shape = QtGui.QPushButton(self.page_regions_overview)
        self.btn_remove_shape.setMinimumSize(QtCore.QSize(30, 0))
        self.btn_remove_shape.setObjectName(_fromUtf8("btn_remove_shape"))
        self.gridLayout_5.addWidget(self.btn_remove_shape, 8, 1, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.ckb_trigger = QtGui.QCheckBox(self.page_regions_overview)
        self.ckb_trigger.setChecked(True)
        self.ckb_trigger.setObjectName(_fromUtf8("ckb_trigger"))
        self.horizontalLayout.addWidget(self.ckb_trigger)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.lbl_x = QtGui.QLabel(self.page_regions_overview)
        self.lbl_x.setObjectName(_fromUtf8("lbl_x"))
        self.horizontalLayout.addWidget(self.lbl_x)
        self.spin_shape_x = QtGui.QSpinBox(self.page_regions_overview)
        self.spin_shape_x.setButtonSymbols(QtGui.QAbstractSpinBox.PlusMinus)
        self.spin_shape_x.setAccelerated(True)
        self.spin_shape_x.setMinimum(-2048)
        self.spin_shape_x.setMaximum(2048)
        self.spin_shape_x.setObjectName(_fromUtf8("spin_shape_x"))
        self.horizontalLayout.addWidget(self.spin_shape_x)
        self.gridLayout_5.addLayout(self.horizontalLayout, 3, 0, 1, 2)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.lbl_y = QtGui.QLabel(self.page_regions_overview)
        self.lbl_y.setObjectName(_fromUtf8("lbl_y"))
        self.horizontalLayout_2.addWidget(self.lbl_y)
        self.spin_shape_y = QtGui.QSpinBox(self.page_regions_overview)
        self.spin_shape_y.setButtonSymbols(QtGui.QAbstractSpinBox.PlusMinus)
        self.spin_shape_y.setAccelerated(True)
        self.spin_shape_y.setMinimum(-2048)
        self.spin_shape_y.setMaximum(2048)
        self.spin_shape_y.setObjectName(_fromUtf8("spin_shape_y"))
        self.horizontalLayout_2.addWidget(self.spin_shape_y)
        self.gridLayout_5.addLayout(self.horizontalLayout_2, 5, 0, 1, 2)
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
        self.gridLayout_5.addWidget(self.tree_region_shapes, 6, 0, 2, 2)
        self.gridLayout_6.addLayout(self.gridLayout_5, 0, 0, 1, 1)
        self.toolBox.addItem(self.page_regions_overview, _fromUtf8(""))
        self.page_regions_collisions = QtGui.QWidget()
        self.page_regions_collisions.setGeometry(QtCore.QRect(0, 0, 239, 259))
        self.page_regions_collisions.setObjectName(_fromUtf8("page_regions_collisions"))
        self.gridLayout_8 = QtGui.QGridLayout(self.page_regions_collisions)
        self.gridLayout_8.setMargin(0)
        self.gridLayout_8.setSpacing(0)
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.gridLayout_10 = QtGui.QGridLayout()
        self.gridLayout_10.setObjectName(_fromUtf8("gridLayout_10"))
        self.table_slots = QtGui.QTableWidget(self.page_regions_collisions)
        self.table_slots.setEnabled(False)
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
        self.btn_lock_table = QtGui.QPushButton(self.page_regions_collisions)
        self.btn_lock_table.setCheckable(True)
        self.btn_lock_table.setDefault(True)
        self.btn_lock_table.setObjectName(_fromUtf8("btn_lock_table"))
        self.gridLayout_10.addWidget(self.btn_lock_table, 0, 0, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout_10, 0, 0, 1, 1)
        self.toolBox.addItem(self.page_regions_collisions, _fromUtf8(""))
        self.page_regions_IO = QtGui.QWidget()
        self.page_regions_IO.setGeometry(QtCore.QRect(0, 0, 239, 259))
        self.page_regions_IO.setObjectName(_fromUtf8("page_regions_IO"))
        self.gridLayout_7 = QtGui.QGridLayout(self.page_regions_IO)
        self.gridLayout_7.setMargin(0)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.gridLayout_9 = QtGui.QGridLayout()
        self.gridLayout_9.setObjectName(_fromUtf8("gridLayout_9"))
        self.combo_label = QtGui.QComboBox(self.page_regions_IO)
        self.combo_label.setEditable(True)
        self.combo_label.setObjectName(_fromUtf8("combo_label"))
        self.gridLayout_9.addWidget(self.combo_label, 0, 1, 1, 2)
        self.pushButton_15 = QtGui.QPushButton(self.page_regions_IO)
        self.pushButton_15.setObjectName(_fromUtf8("pushButton_15"))
        self.gridLayout_9.addWidget(self.pushButton_15, 1, 1, 1, 1)
        self.pushButton_14 = QtGui.QPushButton(self.page_regions_IO)
        self.pushButton_14.setObjectName(_fromUtf8("pushButton_14"))
        self.gridLayout_9.addWidget(self.pushButton_14, 2, 1, 1, 1)
        self.pushButton_13 = QtGui.QPushButton(self.page_regions_IO)
        self.pushButton_13.setObjectName(_fromUtf8("pushButton_13"))
        self.gridLayout_9.addWidget(self.pushButton_13, 2, 2, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_9.addItem(spacerItem2, 3, 1, 2, 2)
        self.pushButton_12 = QtGui.QPushButton(self.page_regions_IO)
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
        tab_regions.setWindowTitle(QtGui.QApplication.translate("tab_regions", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_add_shape.setStatusTip(QtGui.QApplication.translate("tab_regions", "Drag: Rectangle. Shift+drag: Line. Ctrl+drag: Circle.", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_add_shape.setText(QtGui.QApplication.translate("tab_regions", "&Add", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_remove_shape.setText(QtGui.QApplication.translate("tab_regions", "&Remove", None, QtGui.QApplication.UnicodeUTF8))
        self.ckb_trigger.setText(QtGui.QApplication.translate("tab_regions", "Digital trigger on collisions", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_x.setText(QtGui.QApplication.translate("tab_regions", "x:", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_y.setText(QtGui.QApplication.translate("tab_regions", "y:", None, QtGui.QApplication.UnicodeUTF8))
        self.tree_region_shapes.headerItem().setText(0, QtGui.QApplication.translate("tab_regions", "Shapes", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_regions_overview), QtGui.QApplication.translate("tab_regions", "Shapes", None, QtGui.QApplication.UnicodeUTF8))
        item = self.table_slots.horizontalHeaderItem(0)
        item.setText(QtGui.QApplication.translate("tab_regions", "Collision", None, QtGui.QApplication.UnicodeUTF8))
        item = self.table_slots.horizontalHeaderItem(1)
        item.setText(QtGui.QApplication.translate("tab_regions", "Pin", None, QtGui.QApplication.UnicodeUTF8))
        item = self.table_slots.horizontalHeaderItem(2)
        item.setText(QtGui.QApplication.translate("tab_regions", "Logic", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_lock_table.setText(QtGui.QApplication.translate("tab_regions", "Unlock", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_regions_collisions), QtGui.QApplication.translate("tab_regions", "Collision Slots", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_15.setText(QtGui.QApplication.translate("tab_regions", "Open", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_14.setText(QtGui.QApplication.translate("tab_regions", "Clone", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_13.setText(QtGui.QApplication.translate("tab_regions", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_12.setText(QtGui.QApplication.translate("tab_regions", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_regions_IO), QtGui.QApplication.translate("tab_regions", "In/Out", None, QtGui.QApplication.UnicodeUTF8))

