from PySide2.QtWidgets import QMainWindow, QDialog, QHeaderView, QTableWidgetItem
from typing import List, Tuple

from ui.ui_modules.ventana_principal.ventana_principal import Ui_MainWindow
from ui.ventana_de_carga.ventana_de_carga_ui import VentanaCarga
from db.db import Db


class VentanaPrincipal(QMainWindow):

    def __init__(self, *args, **kwargs):
        """Constructor de la clase"""
        super().__init__(*args, **kwargs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.busqueda_ventana: QDialog = VentanaCarga(self)

        # Eventos
        self.events()

    def events(self):
        """Eventos de la ventana Principal, personalizados"""
        self.ui.buscar.clicked.connect(self.buscar_start)

    def showEvent(self, event):
        """Evento que sobrescribimos, muestra la ventana"""
        datos: List[Tuple[str]] = Db().get_datos()

        if datos:
            # Comprobamos si estan desactivados las tablas, si lo están los activamos
            if not self.ui.tablainfo.isEnabled() and not self.ui.tablaMasInfo.isEnabled():
                self.ui.tablainfo.setEnabled(True)
                self.ui.tablaMasInfo.setEnabled(True)

                # Hacemos que coja todo el ancho de la tabla
                for c in range(self.ui.tablainfo.horizontalHeader().count()):
                    self.ui.tablainfo.horizontalHeader().setSectionResizeMode(c, QHeaderView.Stretch)

                for c in range(self.ui.tablaMasInfo.horizontalHeader().count()):
                    self.ui.tablaMasInfo.horizontalHeader().setSectionResizeMode(c, QHeaderView.Stretch)

            # Introducimos el número de filas, según los datos
            self.ui.tablainfo.setRowCount(len(datos))
            self.ui.tablaMasInfo.setRowCount(len(datos))

            # Tabla Información
            for row in range(len(datos)):
                # Ip
                self.ui.tablainfo.setItem(row, 0, QTableWidgetItem(datos[row][0]))
                # Status
                self.ui.tablainfo.setItem(row, 1, QTableWidgetItem(datos[row][1]))

            # Tabla Más Información
            for row in range(len(datos)):
                # Ip
                self.ui.tablaMasInfo.setItem(row, 0, QTableWidgetItem(datos[row][0]))
                # Dispositivo
                self.ui.tablaMasInfo.setItem(row, 1, QTableWidgetItem(datos[row][3]))
                # Sistema Operativo
                self.ui.tablaMasInfo.setItem(row, 2, QTableWidgetItem(datos[row][2]))

        return super().showEvent(event)

    def buscar_start(self):
        """Evento Personalizado, al pulsar un botón"""
        Db().clear()
        self.hide()
        self.busqueda_ventana.exec_()
