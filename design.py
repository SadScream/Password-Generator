# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(320, 122)
        Dialog.setMinimumSize(QtCore.QSize(320, 122))
        Dialog.setMaximumSize(QtCore.QSize(320, 122))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/assets/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("QPushButton {\n"
"border: none;\n"
"background-color: rgb(58, 58, 58);\n"
"color: rgb(208, 208, 208);\n"
"font: 15px Calibri\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"color: white;\n"
"background-color: rgb(20, 20, 20);\n"
"}")
        self.generate = QtWidgets.QPushButton(Dialog)
        self.generate.setGeometry(QtCore.QRect(10, 82, 301, 31))
        self.generate.setStyleSheet("")
        self.generate.setObjectName("generate")
        self.password = QtWidgets.QLabel(Dialog)
        self.password.setGeometry(QtCore.QRect(10, 10, 301, 61))
        self.password.setStyleSheet("QLabel {\n"
"background: qlineargradient(spread:pad, angle:135, x1:0, y1:0, x2:1, y2:0, stop: 0 rgba(79,98,161,1), stop: 0.65 rgba(155,46,217,1));\n"
"qproperty-alignment: AlignCenter;\n"
"font: 22px Calibri;\n"
"}")
        self.password.setText("")
        self.password.setObjectName("password")
        self.copy = QtWidgets.QPushButton(Dialog)
        self.copy.setGeometry(QtCore.QRect(270, 25, 29, 30))
        self.copy.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/assets/copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.copy.setIcon(icon1)
        self.copy.setObjectName("copy")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Password generator"))
        self.generate.setText(_translate("Dialog", "Сгенерировать"))
import resource_rc
