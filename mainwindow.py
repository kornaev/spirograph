# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1108, 440)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.mwLayout_2 = QtWidgets.QVBoxLayout()
        self.mwLayout_2.setObjectName("mwLayout_2")
        self.label_out = QtWidgets.QLabel(self.centralwidget)
        self.label_out.setText("")
        self.label_out.setObjectName("label_out")
        self.mwLayout_2.addWidget(self.label_out)
        self.label_out_final = QtWidgets.QLabel(self.centralwidget)
        self.label_out_final.setText("")
        self.label_out_final.setObjectName("label_out_final")
        self.mwLayout_2.addWidget(self.label_out_final)
        self.label_bg = QtWidgets.QLabel(self.centralwidget)
        self.label_bg.setText("")
        self.label_bg.setObjectName("label_bg")
        self.mwLayout_2.addWidget(self.label_bg)
        self.horizontalLayout_4.addLayout(self.mwLayout_2)
        self.mwLayout = QtWidgets.QVBoxLayout()
        self.mwLayout.setObjectName("mwLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.spinBox_outer_diameter = QtWidgets.QSpinBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_outer_diameter.sizePolicy().hasHeightForWidth())
        self.spinBox_outer_diameter.setSizePolicy(sizePolicy)
        self.spinBox_outer_diameter.setProperty("value", 80)
        self.spinBox_outer_diameter.setObjectName("spinBox_outer_diameter")
        self.horizontalLayout.addWidget(self.spinBox_outer_diameter)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.mwLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.spinBox_inner_diameter = QtWidgets.QSpinBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_inner_diameter.sizePolicy().hasHeightForWidth())
        self.spinBox_inner_diameter.setSizePolicy(sizePolicy)
        self.spinBox_inner_diameter.setProperty("value", 30)
        self.spinBox_inner_diameter.setObjectName("spinBox_inner_diameter")
        self.horizontalLayout_2.addWidget(self.spinBox_inner_diameter)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.mwLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.spinBox_plecho = QtWidgets.QSpinBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_plecho.sizePolicy().hasHeightForWidth())
        self.spinBox_plecho.setSizePolicy(sizePolicy)
        self.spinBox_plecho.setProperty("value", 10)
        self.spinBox_plecho.setObjectName("spinBox_plecho")
        self.horizontalLayout_3.addWidget(self.spinBox_plecho)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.mwLayout.addLayout(self.horizontalLayout_3)
        self.but_draw = QtWidgets.QPushButton(self.centralwidget)
        self.but_draw.setObjectName("but_draw")
        self.mwLayout.addWidget(self.but_draw)
        self.but_save = QtWidgets.QPushButton(self.centralwidget)
        self.but_save.setObjectName("but_save")
        self.mwLayout.addWidget(self.but_save)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.mwLayout.addItem(spacerItem)
        self.horizontalLayout_4.addLayout(self.mwLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.label.setBuddy(self.spinBox_outer_diameter)
        self.label_2.setBuddy(self.spinBox_inner_diameter)
        self.label_3.setBuddy(self.spinBox_plecho)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Спирограф"))
        self.label.setText(_translate("MainWindow", "Диаметр наружной окружности"))
        self.label_2.setText(_translate("MainWindow", "Диаметр внутренней окружности"))
        self.spinBox_plecho.setStatusTip(_translate("MainWindow", "234"))
        self.spinBox_plecho.setWhatsThis(_translate("MainWindow", "345"))
        self.spinBox_plecho.setAccessibleName(_translate("MainWindow", "456"))
        self.label_3.setText(_translate("MainWindow", "Смещение от центра внутренней окружности"))
        self.but_draw.setText(_translate("MainWindow", "Отрисовать"))
        self.but_save.setText(_translate("MainWindow", "Сохранить"))

