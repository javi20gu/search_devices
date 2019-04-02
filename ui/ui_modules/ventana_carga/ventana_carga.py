# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Carga.ui',
# licensing of 'Carga.ui' applies.
#
# Created: Tue Mar 12 00:58:06 2019
#      by: pyside2-uic  running on PySide2 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(656, 122)
        Dialog.setMinimumSize(QtCore.QSize(656, 122))
        Dialog.setMaximumSize(QtCore.QSize(656, 122))
        Dialog.setStyleSheet("#Dialog {\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.text = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(21)
        self.text.setFont(font)
        self.text.setStyleSheet("color: rgb(77, 77, 77)")
        self.text.setObjectName("text")
        self.verticalLayout.addWidget(self.text)
        self.proceso = QtWidgets.QProgressBar(Dialog)
        self.proceso.setStyleSheet("#proceso::chunk {\n"
"    background-color: rgb(136, 136, 136)\n"
"}")
        self.proceso.setMaximum(0)
        self.proceso.setProperty("value", -1)
        self.proceso.setTextVisible(False)
        self.proceso.setObjectName("proceso")
        self.verticalLayout.addWidget(self.proceso)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtWidgets.QApplication.translate("Dialog", "Buscando...", None, -1))
        self.text.setText(QtWidgets.QApplication.translate("Dialog", "Buscando Equipos en la Red...", None, -1))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

