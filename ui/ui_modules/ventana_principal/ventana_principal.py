# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui',
# licensing of 'MainWindow.ui' applies.
#
# Created: Tue Mar 12 00:46:34 2019
#      by: pyside2-uic  running on PySide2 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(807, 522)
        MainWindow.setStyleSheet("#MainWindow {\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tablainfo = QtWidgets.QTableWidget(self.centralwidget)
        self.tablainfo.setEnabled(False)
        self.tablainfo.setStyleSheet("")
        self.tablainfo.setObjectName("tablainfo")
        self.tablainfo.setColumnCount(2)
        self.tablainfo.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tablainfo.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablainfo.setHorizontalHeaderItem(1, item)
        self.horizontalLayout.addWidget(self.tablainfo)
        self.tablaMasInfo = QtWidgets.QTableWidget(self.centralwidget)
        self.tablaMasInfo.setEnabled(False)
        self.tablaMasInfo.setObjectName("tablaMasInfo")
        self.tablaMasInfo.setColumnCount(3)
        self.tablaMasInfo.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tablaMasInfo.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaMasInfo.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaMasInfo.setHorizontalHeaderItem(2, item)
        self.horizontalLayout.addWidget(self.tablaMasInfo)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem)
        self.buscar = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setWeight(75)
        font.setBold(True)
        self.buscar.setFont(font)
        self.buscar.setStyleSheet("#buscar {\n"
"background-color:transparent;\n"
"border: 1.9px solid rgb(71, 158, 168);\n"
"padding: 11px 0;\n"
"border-radius: 3px;\n"
"color: rgb(71, 158, 168);\n"
"}\n"
"#buscar:hover {\n"
"    background-color: rgb(71, 158, 168);\n"
"border: 0px solid  rgb(120, 138, 120);\n"
"color: #fff\n"
"}")
        self.buscar.setObjectName("buscar")
        self.verticalLayout.addWidget(self.buscar)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 807, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setSizeGripEnabled(True)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Busqueda de Dispositivos", None, -1))
        self.tablainfo.horizontalHeaderItem(0).setText(QtWidgets.QApplication.translate("MainWindow", "IP", None, -1))
        self.tablainfo.horizontalHeaderItem(1).setText(QtWidgets.QApplication.translate("MainWindow", "Status", None, -1))
        self.tablaMasInfo.horizontalHeaderItem(0).setText(QtWidgets.QApplication.translate("MainWindow", "IP", None, -1))
        self.tablaMasInfo.horizontalHeaderItem(1).setText(QtWidgets.QApplication.translate("MainWindow", "Dispositivo", None, -1))
        self.tablaMasInfo.horizontalHeaderItem(2).setText(QtWidgets.QApplication.translate("MainWindow", "Sistema Operativo", None, -1))
        self.buscar.setText(QtWidgets.QApplication.translate("MainWindow", "Buscar", None, -1))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

