# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_window(object):
    def setupUi(self, window):
        window.setObjectName("window")
        window.resize(600, 400)
        self.centralwidget = QtWidgets.QWidget(window)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.hl_upper = QtWidgets.QHBoxLayout()
        self.hl_upper.setObjectName("hl_upper")
        self.__mac = QtWidgets.QLabel(self.centralwidget)
        self.__mac.setObjectName("__mac")
        self.hl_upper.addWidget(self.__mac)
        self.mac = QtWidgets.QLineEdit(self.centralwidget)
        self.mac.setObjectName("mac")
        self.hl_upper.addWidget(self.mac)
        self.connect = QtWidgets.QPushButton(self.centralwidget)
        self.connect.setObjectName("connect")
        self.hl_upper.addWidget(self.connect)
        self.gridLayout.addLayout(self.hl_upper, 0, 0, 1, 1)
        self.output = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.output.setObjectName("output")
        self.gridLayout.addWidget(self.output, 1, 0, 1, 1)
        self.hl_lower = QtWidgets.QHBoxLayout()
        self.hl_lower.setObjectName("hl_lower")
        self.command = QtWidgets.QLineEdit(self.centralwidget)
        self.command.setObjectName("command")
        self.hl_lower.addWidget(self.command)
        self.close = QtWidgets.QPushButton(self.centralwidget)
        self.close.setObjectName("close")
        self.hl_lower.addWidget(self.close)
        self.gridLayout.addLayout(self.hl_lower, 2, 0, 1, 1)
        window.setCentralWidget(self.centralwidget)

        self.retranslateUi(window)
        QtCore.QMetaObject.connectSlotsByName(window)
        window.setTabOrder(self.mac, self.command)
        window.setTabOrder(self.command, self.output)

    def retranslateUi(self, window):
        _translate = QtCore.QCoreApplication.translate
        self.__mac.setText(_translate("window", "MAC"))
        self.connect.setText(_translate("window", "Connect"))
        self.close.setText(_translate("window", "Close"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = Ui_window()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())

