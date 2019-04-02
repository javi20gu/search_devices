from PySide2.QtWidgets import QApplication, QMainWindow
from sys import argv, exit

from ui.ventana_principal.ventana_principal_ui import VentanaPrincipal
from db.db import Db

if __name__ == "__main__":
    Db().create_table()
    run_app: QApplication = QApplication(argv)
    ventana_principal: QMainWindow = VentanaPrincipal()
    ventana_principal.show()
    exit(run_app.exec_())
