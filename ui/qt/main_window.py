# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(543, 503)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.row_9 = QtWidgets.QHBoxLayout()
        self.row_9.setObjectName("row_9")
        self.row_button_10 = QtWidgets.QPushButton(self.centralwidget)
        self.row_button_10.setMinimumSize(QtCore.QSize(48, 28))
        self.row_button_10.setMaximumSize(QtCore.QSize(48, 28))
        self.row_button_10.setObjectName("row_button_10")
        self.row_9.addWidget(self.row_button_10)
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.row_9.addItem(spacerItem)
        self.verticalLayout.addLayout(self.row_9)
        self.row_0 = QtWidgets.QHBoxLayout()
        self.row_0.setObjectName("row_0")
        self.row_button_0 = QtWidgets.QPushButton(self.centralwidget)
        self.row_button_0.setMinimumSize(QtCore.QSize(48, 28))
        self.row_button_0.setMaximumSize(QtCore.QSize(48, 28))
        self.row_button_0.setObjectName("row_button_0")
        self.row_0.addWidget(self.row_button_0)
        self.row_label_0 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(20)
        self.row_label_0.setFont(font)
        self.row_label_0.setText("")
        self.row_label_0.setObjectName("row_label_0")
        self.row_0.addWidget(self.row_label_0)
        self.verticalLayout.addLayout(self.row_0)
        self.row_1 = QtWidgets.QHBoxLayout()
        self.row_1.setObjectName("row_1")
        self.row_button_1 = QtWidgets.QPushButton(self.centralwidget)
        self.row_button_1.setMinimumSize(QtCore.QSize(48, 28))
        self.row_button_1.setMaximumSize(QtCore.QSize(48, 28))
        self.row_button_1.setObjectName("row_button_1")
        self.row_1.addWidget(self.row_button_1)
        self.row_label_1 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(20)
        self.row_label_1.setFont(font)
        self.row_label_1.setText("")
        self.row_label_1.setObjectName("row_label_1")
        self.row_1.addWidget(self.row_label_1)
        self.verticalLayout.addLayout(self.row_1)
        self.row_2 = QtWidgets.QHBoxLayout()
        self.row_2.setObjectName("row_2")
        self.row_button_2 = QtWidgets.QPushButton(self.centralwidget)
        self.row_button_2.setMinimumSize(QtCore.QSize(48, 28))
        self.row_button_2.setMaximumSize(QtCore.QSize(48, 28))
        self.row_button_2.setObjectName("row_button_2")
        self.row_2.addWidget(self.row_button_2)
        self.row_label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(20)
        self.row_label_2.setFont(font)
        self.row_label_2.setText("")
        self.row_label_2.setObjectName("row_label_2")
        self.row_2.addWidget(self.row_label_2)
        self.verticalLayout.addLayout(self.row_2)
        self.row_3 = QtWidgets.QHBoxLayout()
        self.row_3.setObjectName("row_3")
        self.row_button_3 = QtWidgets.QPushButton(self.centralwidget)
        self.row_button_3.setMinimumSize(QtCore.QSize(48, 28))
        self.row_button_3.setMaximumSize(QtCore.QSize(48, 28))
        self.row_button_3.setObjectName("row_button_3")
        self.row_3.addWidget(self.row_button_3)
        self.row_label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(20)
        self.row_label_3.setFont(font)
        self.row_label_3.setText("")
        self.row_label_3.setObjectName("row_label_3")
        self.row_3.addWidget(self.row_label_3)
        self.verticalLayout.addLayout(self.row_3)
        self.row_4 = QtWidgets.QHBoxLayout()
        self.row_4.setObjectName("row_4")
        self.row_button_4 = QtWidgets.QPushButton(self.centralwidget)
        self.row_button_4.setMinimumSize(QtCore.QSize(48, 28))
        self.row_button_4.setMaximumSize(QtCore.QSize(48, 28))
        self.row_button_4.setObjectName("row_button_4")
        self.row_4.addWidget(self.row_button_4)
        self.row_label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(20)
        self.row_label_4.setFont(font)
        self.row_label_4.setText("")
        self.row_label_4.setObjectName("row_label_4")
        self.row_4.addWidget(self.row_label_4)
        self.verticalLayout.addLayout(self.row_4)
        self.row_5 = QtWidgets.QHBoxLayout()
        self.row_5.setObjectName("row_5")
        self.row_button_5 = QtWidgets.QPushButton(self.centralwidget)
        self.row_button_5.setMinimumSize(QtCore.QSize(48, 28))
        self.row_button_5.setMaximumSize(QtCore.QSize(48, 28))
        self.row_button_5.setObjectName("row_button_5")
        self.row_5.addWidget(self.row_button_5)
        self.row_label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(20)
        self.row_label_5.setFont(font)
        self.row_label_5.setText("")
        self.row_label_5.setObjectName("row_label_5")
        self.row_5.addWidget(self.row_label_5)
        self.verticalLayout.addLayout(self.row_5)
        self.row_6 = QtWidgets.QHBoxLayout()
        self.row_6.setObjectName("row_6")
        self.row_button_6 = QtWidgets.QPushButton(self.centralwidget)
        self.row_button_6.setMinimumSize(QtCore.QSize(48, 28))
        self.row_button_6.setMaximumSize(QtCore.QSize(48, 28))
        self.row_button_6.setObjectName("row_button_6")
        self.row_6.addWidget(self.row_button_6)
        self.row_label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(20)
        self.row_label_6.setFont(font)
        self.row_label_6.setText("")
        self.row_label_6.setObjectName("row_label_6")
        self.row_6.addWidget(self.row_label_6)
        self.verticalLayout.addLayout(self.row_6)
        self.row_7 = QtWidgets.QHBoxLayout()
        self.row_7.setObjectName("row_7")
        self.row_button_7 = QtWidgets.QPushButton(self.centralwidget)
        self.row_button_7.setMinimumSize(QtCore.QSize(48, 28))
        self.row_button_7.setMaximumSize(QtCore.QSize(48, 28))
        self.row_button_7.setObjectName("row_button_7")
        self.row_7.addWidget(self.row_button_7)
        self.row_label_7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(20)
        self.row_label_7.setFont(font)
        self.row_label_7.setText("")
        self.row_label_7.setObjectName("row_label_7")
        self.row_7.addWidget(self.row_label_7)
        self.verticalLayout.addLayout(self.row_7)
        self.row_8 = QtWidgets.QHBoxLayout()
        self.row_8.setObjectName("row_8")
        self.row_button_9 = QtWidgets.QPushButton(self.centralwidget)
        self.row_button_9.setMinimumSize(QtCore.QSize(48, 28))
        self.row_button_9.setMaximumSize(QtCore.QSize(48, 28))
        self.row_button_9.setObjectName("row_button_9")
        self.row_8.addWidget(self.row_button_9)
        self.row_label_8 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(20)
        self.row_label_8.setFont(font)
        self.row_label_8.setText("")
        self.row_label_8.setObjectName("row_label_8")
        self.row_8.addWidget(self.row_label_8)
        self.verticalLayout.addLayout(self.row_8)
        self.row_10 = QtWidgets.QHBoxLayout()
        self.row_10.setObjectName("row_10")
        self.row_button_11 = QtWidgets.QPushButton(self.centralwidget)
        self.row_button_11.setMinimumSize(QtCore.QSize(48, 28))
        self.row_button_11.setMaximumSize(QtCore.QSize(48, 28))
        self.row_button_11.setObjectName("row_button_11")
        self.row_10.addWidget(self.row_button_11)
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.row_10.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.row_10)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        spacerItem3 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 543, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.toolBar_2 = QtWidgets.QToolBar(MainWindow)
        self.toolBar_2.setObjectName("toolBar_2")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_2)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.row_button_10.setText(_translate("MainWindow", "R"))
        self.row_button_0.setText(_translate("MainWindow", "1"))
        self.row_button_1.setText(_translate("MainWindow", "2"))
        self.row_button_2.setText(_translate("MainWindow", "3"))
        self.row_button_3.setText(_translate("MainWindow", "4"))
        self.row_button_4.setText(_translate("MainWindow", "5"))
        self.row_button_5.setText(_translate("MainWindow", "6"))
        self.row_button_6.setText(_translate("MainWindow", "7"))
        self.row_button_7.setText(_translate("MainWindow", "8"))
        self.row_button_9.setText(_translate("MainWindow", "9"))
        self.row_button_11.setText(_translate("MainWindow", "X"))
        self.pushButton.setText(_translate("MainWindow", "<"))
        self.pushButton_2.setText(_translate("MainWindow", "L"))
        self.pushButton_3.setText(_translate("MainWindow", ">"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.toolBar_2.setWindowTitle(_translate("MainWindow", "toolBar_2"))
