# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tab_objectsUi.ui'
#
# Created: Mon Mar 31 00:57:39 2014
#      by: PyQt4 UI code generator 4.10.4
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

class Ui_tab_objects(object):
    def setupUi(self, tab_objects):
        tab_objects.setObjectName(_fromUtf8("tab_objects"))
        tab_objects.resize(249, 413)
        self.gridLayout = QtGui.QGridLayout(tab_objects)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setSpacing(1)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.toolBox = QtGui.QToolBox(tab_objects)
        self.toolBox.setFrameShape(QtGui.QFrame.NoFrame)
        self.toolBox.setFrameShadow(QtGui.QFrame.Plain)
        self.toolBox.setLineWidth(0)
        self.toolBox.setObjectName(_fromUtf8("toolBox"))
        self.page_objects_tracking = QtGui.QWidget()
        self.page_objects_tracking.setGeometry(QtCore.QRect(0, 0, 247, 369))
        self.page_objects_tracking.setObjectName(_fromUtf8("page_objects_tracking"))
        self.gridLayout_6 = QtGui.QGridLayout(self.page_objects_tracking)
        self.gridLayout_6.setMargin(0)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.gridLayout_5 = QtGui.QGridLayout()
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setContentsMargins(-1, 0, -1, -1)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.gridLayout_10 = QtGui.QGridLayout()
        self.gridLayout_10.setSpacing(0)
        self.gridLayout_10.setObjectName(_fromUtf8("gridLayout_10"))
        self.table_slots = QtGui.QTableWidget(self.page_objects_tracking)
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
        self.table_slots.verticalHeader().setDefaultSectionSize(10)
        self.gridLayout_10.addWidget(self.table_slots, 0, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_10, 4, 0, 1, 5)
        self.lbl_x = QtGui.QLabel(self.page_objects_tracking)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_x.sizePolicy().hasHeightForWidth())
        self.lbl_x.setSizePolicy(sizePolicy)
        self.lbl_x.setMinimumSize(QtCore.QSize(32, 0))
        self.lbl_x.setMaximumSize(QtCore.QSize(32, 16777215))
        self.lbl_x.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_x.setObjectName(_fromUtf8("lbl_x"))
        self.gridLayout_5.addWidget(self.lbl_x, 0, 4, 1, 1)
        self.lbl_y_lbl = QtGui.QLabel(self.page_objects_tracking)
        self.lbl_y_lbl.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_y_lbl.setObjectName(_fromUtf8("lbl_y_lbl"))
        self.gridLayout_5.addWidget(self.lbl_y_lbl, 1, 3, 1, 1)
        self.lbl_y = QtGui.QLabel(self.page_objects_tracking)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_y.sizePolicy().hasHeightForWidth())
        self.lbl_y.setSizePolicy(sizePolicy)
        self.lbl_y.setMinimumSize(QtCore.QSize(32, 0))
        self.lbl_y.setMaximumSize(QtCore.QSize(32, 16777215))
        self.lbl_y.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_y.setObjectName(_fromUtf8("lbl_y"))
        self.gridLayout_5.addWidget(self.lbl_y, 1, 4, 1, 1)
        self.lbl_xlbl = QtGui.QLabel(self.page_objects_tracking)
        self.lbl_xlbl.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_xlbl.setObjectName(_fromUtf8("lbl_xlbl"))
        self.gridLayout_5.addWidget(self.lbl_xlbl, 0, 3, 1, 1)
        self.lbl_speed_lbl = QtGui.QLabel(self.page_objects_tracking)
        self.lbl_speed_lbl.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_speed_lbl.setObjectName(_fromUtf8("lbl_speed_lbl"))
        self.gridLayout_5.addWidget(self.lbl_speed_lbl, 2, 3, 1, 1)
        self.ckb_track = QtGui.QCheckBox(self.page_objects_tracking)
        self.ckb_track.setChecked(True)
        self.ckb_track.setObjectName(_fromUtf8("ckb_track"))
        self.gridLayout_5.addWidget(self.ckb_track, 1, 0, 1, 1)
        self.ckb_analog_pos = QtGui.QCheckBox(self.page_objects_tracking)
        self.ckb_analog_pos.setObjectName(_fromUtf8("ckb_analog_pos"))
        self.gridLayout_5.addWidget(self.ckb_analog_pos, 0, 0, 1, 1)
        self.ckb_trace = QtGui.QCheckBox(self.page_objects_tracking)
        self.ckb_trace.setChecked(True)
        self.ckb_trace.setObjectName(_fromUtf8("ckb_trace"))
        self.gridLayout_5.addWidget(self.ckb_trace, 2, 0, 1, 1)
        self.dial_direction = QtGui.QDial(self.page_objects_tracking)
        self.dial_direction.setEnabled(False)
        self.dial_direction.setMaximum(359)
        self.dial_direction.setPageStep(1)
        self.dial_direction.setOrientation(QtCore.Qt.Vertical)
        self.dial_direction.setInvertedAppearance(False)
        self.dial_direction.setWrapping(True)
        self.dial_direction.setNotchTarget(20.0)
        self.dial_direction.setNotchesVisible(True)
        self.dial_direction.setObjectName(_fromUtf8("dial_direction"))
        self.gridLayout_5.addWidget(self.dial_direction, 0, 1, 3, 2)
        self.tree_link_features = QtGui.QTreeWidget(self.page_objects_tracking)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tree_link_features.sizePolicy().hasHeightForWidth())
        self.tree_link_features.setSizePolicy(sizePolicy)
        self.tree_link_features.setProperty("showDropIndicator", False)
        self.tree_link_features.setAlternatingRowColors(True)
        self.tree_link_features.setIndentation(0)
        self.tree_link_features.setObjectName(_fromUtf8("tree_link_features"))
        self.tree_link_features.header().setSortIndicatorShown(False)
        self.gridLayout_5.addWidget(self.tree_link_features, 3, 0, 1, 5)
        self.lbl_speed = QtGui.QLabel(self.page_objects_tracking)
        self.lbl_speed.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_speed.setObjectName(_fromUtf8("lbl_speed"))
        self.gridLayout_5.addWidget(self.lbl_speed, 2, 4, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_5, 0, 0, 1, 1)
        self.toolBox.addItem(self.page_objects_tracking, _fromUtf8(""))
        self.page_objects_IO = QtGui.QWidget()
        self.page_objects_IO.setGeometry(QtCore.QRect(0, 0, 247, 369))
        self.page_objects_IO.setObjectName(_fromUtf8("page_objects_IO"))
        self.gridLayout_7 = QtGui.QGridLayout(self.page_objects_IO)
        self.gridLayout_7.setMargin(0)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.pushButton_8 = QtGui.QPushButton(self.page_objects_IO)
        self.pushButton_8.setEnabled(False)
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.gridLayout_3.addWidget(self.pushButton_8, 1, 1, 1, 1)
        self.pushButton_5 = QtGui.QPushButton(self.page_objects_IO)
        self.pushButton_5.setEnabled(False)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.gridLayout_3.addWidget(self.pushButton_5, 2, 1, 1, 1)
        self.pushButton_4 = QtGui.QPushButton(self.page_objects_IO)
        self.pushButton_4.setEnabled(False)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.gridLayout_3.addWidget(self.pushButton_4, 2, 0, 1, 1)
        self.pushButton_9 = QtGui.QPushButton(self.page_objects_IO)
        self.pushButton_9.setEnabled(False)
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
        self.gridLayout_3.addWidget(self.pushButton_9, 1, 0, 1, 1)
        self.combo_label = QtGui.QComboBox(self.page_objects_IO)
        self.combo_label.setEnabled(False)
        self.combo_label.setEditable(True)
        self.combo_label.setObjectName(_fromUtf8("combo_label"))
        self.gridLayout_3.addWidget(self.combo_label, 0, 0, 1, 2)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 3, 0, 2, 2)
        self.gridLayout_7.addLayout(self.gridLayout_3, 0, 2, 1, 1)
        self.toolBox.addItem(self.page_objects_IO, _fromUtf8(""))
        self.gridLayout_2.addWidget(self.toolBox, 1, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        self.retranslateUi(tab_objects)
        self.toolBox.setCurrentIndex(0)
        self.toolBox.layout().setSpacing(0)
        QtCore.QMetaObject.connectSlotsByName(tab_objects)

    def retranslateUi(self, tab_objects):
        tab_objects.setWindowTitle(_translate("tab_objects", "Form", None))
        item = self.table_slots.horizontalHeaderItem(0)
        item.setText(_translate("tab_objects", "Property", None))
        item = self.table_slots.horizontalHeaderItem(1)
        item.setText(_translate("tab_objects", "Pin", None))
        item = self.table_slots.horizontalHeaderItem(2)
        item.setText(_translate("tab_objects", "Logic", None))
        self.lbl_x.setText(_translate("tab_objects", "---", None))
        self.lbl_y_lbl.setText(_translate("tab_objects", "y:", None))
        self.lbl_y.setText(_translate("tab_objects", "---", None))
        self.lbl_xlbl.setText(_translate("tab_objects", "x:", None))
        self.lbl_speed_lbl.setText(_translate("tab_objects", "v:", None))
        self.ckb_track.setText(_translate("tab_objects", "Track", None))
        self.ckb_analog_pos.setText(_translate("tab_objects", "Analog out", None))
        self.ckb_trace.setText(_translate("tab_objects", "Show Trace", None))
        self.tree_link_features.headerItem().setText(0, _translate("tab_objects", "Features", None))
        self.lbl_speed.setText(_translate("tab_objects", "---", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_objects_tracking), _translate("tab_objects", "Tracking", None))
        self.pushButton_8.setText(_translate("tab_objects", "Save", None))
        self.pushButton_5.setText(_translate("tab_objects", "Delete", None))
        self.pushButton_4.setText(_translate("tab_objects", "Clone", None))
        self.pushButton_9.setText(_translate("tab_objects", "Open", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_objects_IO), _translate("tab_objects", "In/Out", None))

