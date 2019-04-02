from PySide2.QtWidgets import QDialog, QMainWindow
from PySide2.QtCore import QThread, Slot

from ui.ui_modules.ventana_carga.ventana_carga import Ui_Dialog
from modules.thread.thread_module import ThreadBusqueda


class VentanaCarga(QDialog):

    def __init__(self, padre: QMainWindow, *args, **kwargs):
        """Constructor de la clase"""
        super().__init__(*args, **kwargs)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.padre: QMainWindow = padre
        self.hilo: QThread = ThreadBusqueda()

    @Slot(None)
    def proceso_finalizado(self):
        self.close()

    def showEvent(self, event):
        """Evento SobreCargado, Muestra la ventana"""
        self.hilo.start()
        self.hilo.finished.connect(self.proceso_finalizado)
        return super().showEvent(event)

    def closeEvent(self, event):
        """Evento SobreCargado, Cierra la ventana"""
        self.padre.show()
        return super().closeEvent(event)
