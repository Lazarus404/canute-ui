# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created: Wed Jul 19 17:48:37 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(543, 503)
        sizePolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtGui.QWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.row_9 = QtGui.QHBoxLayout()
        self.row_9.setObjectName("row_9")
        self.row_button_10 = QtGui.QPushButton(self.centralwidget)
        self.row_button_10.setMinimumSize(QtCore.QSize(48, 28))
        self.row_button_10.setMaximumSize(QtCore.QSize(48, 28))
        self.row_button_10.setObjectName("row_button_10")
        self.row_9.addWidget(self.row_button_10)
        spacerItem = QtGui.QSpacerItem(
            40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.row_9.addItem(spacerItem)
        self.verticalLayout.addLayout(self.row_9)
        self.row_0 = QtGui.QHBoxLayout()
        self.row_0.setObjectName("row_0")
        self.row_button_0 = QtGui.QPushButton(self.centralwidget)
        self.row_button_0.setMinimumSize(QtCore.QSize(48, 28))
        self.row_button_0.setMaximumSize(QtCore.QSize(48, 28))
        self.row_button_0.setObjectName("row_button_0")
        self.row_0.addWidget(self.row_button_0)
        self.row_label_0 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(20)
        self.row_label_0.setFont(font)
        self.row_label_0.setText("")
        self.row_label_0.setObjectName("row_label_0")
        self.row_0.addWidget(self.row_label_0)
        self.verticalLayout.addLayout(self.row_0)
        self.row_1 = QtGui.QHBoxLayout()
        self.row_1.setObjectName("row_1")
        self.row_button_1 = QtGui.QPushButton(self.centralwidget)
        self.row_button_1.setMinimumSize(QtCore.QSize(48, 28))
        self.row_button_1.setMaximumSize(QtCore.QSize(48, 28))
        self.row_button_1.setObjectName("row_button_1")
        self.row_1.addWidget(self.row_button_1)
        self.row_label_1 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(20)
        self.row_label_1.setFont(font)
        self.row_label_1.setText("")
        self.row_label_1.setObjectName("row_label_1")
        self.row_1.addWidget(self.row_label_1)
        self.verticalLayout.addLayout(self.row_1)
        self.row_2 = QtGui.QHBoxLayout()
        self.row_2.setObjectName("row_2")
        self.row_button_2 = QtGui.QPushButton(self.centralwidget)
        self.row_button_2.setMinimumSize(QtCore.QSize(48, 28))
        self.row_button_2.setMaximumSize(QtCore.QSize(48, 28))
        self.row_button_2.setObjectName("row_button_2")
        self.row_2.addWidget(self.row_button_2)
        self.row_label_2 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(20)
        self.row_label_2.setFont(font)
        self.row_label_2.setText("")
        self.row_label_2.setObjectName("row_label_2")
        self.row_2.addWidget(self.row_label_2)
        self.verticalLayout.addLayout(self.row_2)
        self.row_3 = QtGui.QHBoxLayout()
        self.row_3.setObjectName("row_3")
        self.row_button_3 = QtGui.QPushButton(self.centralwidget)
        self.row_button_3.setMinimumSize(QtCore.QSize(48, 28))
        self.row_button_3.setMaximumSize(QtCore.QSize(48, 28))
        self.row_button_3.setObjectName("row_button_3")
        self.row_3.addWidget(self.row_button_3)
        self.row_label_3 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(20)
        self.row_label_3.setFont(font)
        self.row_label_3.setText("")
        self.row_label_3.setObjectName("row_label_3")
        self.row_3.addWidget(self.row_label_3)
        self.verticalLayout.addLayout(self.row_3)
        self.row_4 = QtGui.QHBoxLayout()
        self.row_4.setObjectName("row_4")
        self.row_button_4 = QtGui.QPushButton(self.centralwidget)
        self.row_button_4.setMinimumSize(QtCore.QSize(48, 28))
        self.row_button_4.setMaximumSize(QtCore.QSize(48, 28))
        self.row_button_4.setObjectName("row_button_4")
        self.row_4.addWidget(self.row_button_4)
        self.row_label_4 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(20)
        self.row_label_4.setFont(font)
        self.row_label_4.setText("")
        self.row_label_4.setObjectName("row_label_4")
        self.row_4.addWidget(self.row_label_4)
        self.verticalLayout.addLayout(self.row_4)
        self.row_5 = QtGui.QHBoxLayout()
        self.row_5.setObjectName("row_5")
        self.row_button_5 = QtGui.QPushButton(self.centralwidget)
        self.row_button_5.setMinimumSize(QtCore.QSize(48, 28))
        self.row_button_5.setMaximumSize(QtCore.QSize(48, 28))
        self.row_button_5.setObjectName("row_button_5")
        self.row_5.addWidget(self.row_button_5)
        self.row_label_5 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(20)
        self.row_label_5.setFont(font)
        self.row_label_5.setText("")
        self.row_label_5.setObjectName("row_label_5")
        self.row_5.addWidget(self.row_label_5)
        self.verticalLayout.addLayout(self.row_5)
        self.row_6 = QtGui.QHBoxLayout()
        self.row_6.setObjectName("row_6")
        self.row_button_6 = QtGui.QPushButton(self.centralwidget)
        self.row_button_6.setMinimumSize(QtCore.QSize(48, 28))
        self.row_button_6.setMaximumSize(QtCore.QSize(48, 28))
        self.row_button_6.setObjectName("row_button_6")
        self.row_6.addWidget(self.row_button_6)
        self.row_label_6 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(20)
        self.row_label_6.setFont(font)
        self.row_label_6.setText("")
        self.row_label_6.setObjectName("row_label_6")
        self.row_6.addWidget(self.row_label_6)
        self.verticalLayout.addLayout(self.row_6)
        self.row_7 = QtGui.QHBoxLayout()
        self.row_7.setObjectName("row_7")
        self.row_button_7 = QtGui.QPushButton(self.centralwidget)
        self.row_button_7.setMinimumSize(QtCore.QSize(48, 28))
        self.row_button_7.setMaximumSize(QtCore.QSize(48, 28))
        self.row_button_7.setObjectName("row_button_7")
        self.row_7.addWidget(self.row_button_7)
        self.row_label_7 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(20)
        self.row_label_7.setFont(font)
        self.row_label_7.setText("")
        self.row_label_7.setObjectName("row_label_7")
        self.row_7.addWidget(self.row_label_7)
        self.verticalLayout.addLayout(self.row_7)
        self.row_8 = QtGui.QHBoxLayout()
        self.row_8.setObjectName("row_8")
        self.row_button_9 = QtGui.QPushButton(self.centralwidget)
        self.row_button_9.setMinimumSize(QtCore.QSize(48, 28))
        self.row_button_9.setMaximumSize(QtCore.QSize(48, 28))
        self.row_button_9.setObjectName("row_button_9")
        self.row_8.addWidget(self.row_button_9)
        self.row_label_8 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(20)
        self.row_label_8.setFont(font)
        self.row_label_8.setText("")
        self.row_label_8.setObjectName("row_label_8")
        self.row_8.addWidget(self.row_label_8)
        self.verticalLayout.addLayout(self.row_8)
        self.row_10 = QtGui.QHBoxLayout()
        self.row_10.setObjectName("row_10")
        self.row_button_11 = QtGui.QPushButton(self.centralwidget)
        self.row_button_11.setMinimumSize(QtCore.QSize(48, 28))
        self.row_button_11.setMaximumSize(QtCore.QSize(48, 28))
        self.row_button_11.setObjectName("row_button_11")
        self.row_10.addWidget(self.row_button_11)
        spacerItem1 = QtGui.QSpacerItem(
            40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.row_10.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.row_10)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtGui.QSpacerItem(
            40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        spacerItem3 = QtGui.QSpacerItem(
            40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 543, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.toolBar_2 = QtGui.QToolBar(MainWindow)
        self.toolBar_2.setObjectName("toolBar_2")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_2)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate(
            "MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.row_button_10.setText(QtGui.QApplication.translate(
            "MainWindow", "R", None, QtGui.QApplication.UnicodeUTF8))
        self.row_button_0.setText(QtGui.QApplication.translate(
            "MainWindow", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.row_button_1.setText(QtGui.QApplication.translate(
            "MainWindow", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.row_button_2.setText(QtGui.QApplication.translate(
            "MainWindow", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.row_button_3.setText(QtGui.QApplication.translate(
            "MainWindow", "4", None, QtGui.QApplication.UnicodeUTF8))
        self.row_button_4.setText(QtGui.QApplication.translate(
            "MainWindow", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.row_button_5.setText(QtGui.QApplication.translate(
            "MainWindow", "6", None, QtGui.QApplication.UnicodeUTF8))
        self.row_button_6.setText(QtGui.QApplication.translate(
            "MainWindow", "7", None, QtGui.QApplication.UnicodeUTF8))
        self.row_button_7.setText(QtGui.QApplication.translate(
            "MainWindow", "8", None, QtGui.QApplication.UnicodeUTF8))
        self.row_button_9.setText(QtGui.QApplication.translate(
            "MainWindow", "9", None, QtGui.QApplication.UnicodeUTF8))
        self.row_button_11.setText(QtGui.QApplication.translate(
            "MainWindow", "X", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate(
            "MainWindow", "<", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate(
            "MainWindow", "L", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate(
            "MainWindow", ">", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate(
            "MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar_2.setWindowTitle(QtGui.QApplication.translate(
            "MainWindow", "toolBar_2", None, QtGui.QApplication.UnicodeUTF8))
