# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Competition(object):
    def setupUi(self, Competition):
        Competition.setObjectName("Competition")
        Competition.resize(1045, 579)
        Competition.setIconSize(QtCore.QSize(24, 24))
        Competition.setAnimated(False)
        self.centralwidget = QtWidgets.QWidget(Competition)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(40, 500, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 130, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Caslon Pro Bold")
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 170, 241, 151))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(400, 60, 91, 31))
        self.label_4.setObjectName("label_4")
        self.image_1 = QtWidgets.QLabel(self.centralwidget)
        self.image_1.setGeometry(QtCore.QRect(280, 110, 341, 291))
        self.image_1.setStyleSheet("")
        self.image_1.setText("")
        self.image_1.setObjectName("image_1")
        self.image_2 = QtWidgets.QLabel(self.centralwidget)
        self.image_2.setGeometry(QtCore.QRect(650, 110, 341, 291))
        self.image_2.setStyleSheet("")
        self.image_2.setText("")
        self.image_2.setObjectName("image_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(780, 60, 101, 31))
        self.label_5.setObjectName("label_5")
        Competition.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Competition)
        self.statusbar.setObjectName("statusbar")
        Competition.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(Competition)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1045, 23))
        self.menuBar.setObjectName("menuBar")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menuBar)
        self.menu_2.setObjectName("menu_2")
        Competition.setMenuBar(self.menuBar)
        self.actionOpen_one_image_file = QtWidgets.QAction(Competition)
        self.actionOpen_one_image_file.setIconVisibleInMenu(True)
        self.actionOpen_one_image_file.setObjectName("actionOpen_one_image_file")
        self.actionExit = QtWidgets.QAction(Competition)
        self.actionExit.setObjectName("actionExit")
        self.actionAbout_us = QtWidgets.QAction(Competition)
        self.actionAbout_us.setObjectName("actionAbout_us")
        self.actionVersion = QtWidgets.QAction(Competition)
        self.actionVersion.setObjectName("actionVersion")
        self.menu.addSeparator()
        self.menu.addAction(self.actionOpen_one_image_file)
        self.menu.addSeparator()
        self.menu.addAction(self.actionExit)
        self.menu.addSeparator()
        self.menu_2.addAction(self.actionAbout_us)
        self.menu_2.addAction(self.actionVersion)
        self.menuBar.addAction(self.menu.menuAction())
        self.menuBar.addAction(self.menu_2.menuAction())

        self.retranslateUi(Competition)
        QtCore.QMetaObject.connectSlotsByName(Competition)

    def retranslateUi(self, Competition):
        _translate = QtCore.QCoreApplication.translate
        Competition.setWindowTitle(_translate("Competition", "MainWindow"))
        self.pushButton.setText(_translate("Competition", "PushButton"))
        self.label.setText(_translate("Competition", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#00007f;\">参赛学校：湖北文理学院</span></p></body></html>"))
        self.label_3.setText(_translate("Competition", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#00007f;\">参赛队伍：湖文析影</span></p><p><span style=\" font-size:11pt; font-weight:600; color:#00007f;\">指导老师：朱丽娟，谢志远</span></p><p><span style=\" font-size:11pt; font-weight:600; color:#00007f;\">队长：王贤涛</span></p><p><span style=\" font-size:11pt; font-weight:600; color:#00007f;\">队员：杨兰兰，余雪银</span></p></body></html>"))
        self.label_4.setText(_translate("Competition", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">原始图像</span></p></body></html>"))
        self.label_5.setText(_translate("Competition", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">处理后得图像</span></p></body></html>"))
        self.menu.setTitle(_translate("Competition", "File"))
        self.menu_2.setTitle(_translate("Competition", "Help"))
        self.actionOpen_one_image_file.setText(_translate("Competition", "Open one image file"))
        self.actionOpen_one_image_file.setIconText(_translate("Competition", "Open one image file"))
        self.actionExit.setText(_translate("Competition", "Exit"))
        self.actionAbout_us.setText(_translate("Competition", "About us"))
        self.actionVersion.setText(_translate("Competition", "Version"))

