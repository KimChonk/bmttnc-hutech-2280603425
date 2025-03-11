# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './UI/caesar.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import os
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = './platforms'

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 10, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 120, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 280, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(100, 230, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.plainTextTxt = QtWidgets.QTextEdit(self.centralwidget)
        self.plainTextTxt.setGeometry(QtCore.QRect(150, 120, 461, 91))
        self.plainTextTxt.setObjectName("plainTextTxt")
        self.KeyTxt = QtWidgets.QTextEdit(self.centralwidget)
        self.KeyTxt.setGeometry(QtCore.QRect(150, 220, 461, 41))
        self.KeyTxt.setObjectName("KeyTxt")
        self.CiphertextTxt = QtWidgets.QTextEdit(self.centralwidget)
        self.CiphertextTxt.setGeometry(QtCore.QRect(150, 280, 461, 71))
        self.CiphertextTxt.setObjectName("CiphertextTxt")
        self.EncryptBtn = QtWidgets.QPushButton(self.centralwidget)
        self.EncryptBtn.setGeometry(QtCore.QRect(150, 382, 101, 41))
        self.EncryptBtn.setObjectName("EncryptBtn")
        self.DecryptBtn = QtWidgets.QPushButton(self.centralwidget)
        self.DecryptBtn.setGeometry(QtCore.QRect(510, 380, 101, 41))
        self.DecryptBtn.setObjectName("DecryptBtn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "CAESAR CIPHER"))
        self.label_2.setText(_translate("MainWindow", "Plain text"))
        self.label_3.setText(_translate("MainWindow", "Cipher text"))
        self.label_4.setText(_translate("MainWindow", "Key"))
        self.EncryptBtn.setText(_translate("MainWindow", "Encrypt"))
        self.DecryptBtn.setText(_translate("MainWindow", "Decrypt"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
