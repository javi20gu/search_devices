from PySide2.QtWidgets import QDialog
from PySide2.QtCore import QThread, Signal
from socket import gethostname, gethostbyname
from typing import List, Dict, Pattern
from pythonping import ping
from subprocess import Popen, PIPE
from re import compile

from db.db import Db


class ThreadBusqueda(QThread):

    finished: Signal(None)

    def run(self):
        """Evento en el que empieza a ejecutar"""

        # Obtiene el nombre del dispositivo
        nombre_device: str = gethostname()
        # Obtiene la ip mediante nuestro nombre de equipo
        ip: str = gethostbyname(nombre_device)[:gethostbyname(nombre_device).rfind('.')]
        # Obtiene los datos de cada ip dada
        datos_todos: List[Dict[str, str]] = [next(self.getDevice('{}.{}'.format(ip, i))) for i in range(255)]
        # Nos filtra las conexiones 'online'
        datos: List[None] = [Db().introducir_valores(dato['ip'], dato['status'], dato['sistema_operativo'],
                                                      dato['dispositivo'])
                 for dato in datos_todos if dato["status"] == 'online']
        # Emitimos la señal
        self.finished.emit()

    def getDevice(self, ip: str) -> Dict[str, str]:
        """Obtenemos los datos mediante una ip"""

        okey: str = str(ping(ip, timeout=0.15))

        if okey.rfind('0') == 126:
            yield {
                'status': 'offline',
                'ip': ip
            }

        else:
            from socket import getfqdn
            p: Popen = Popen(["ping", ip], stdout=PIPE)
            res: str = p.communicate()[0]
            pattern: Pattern = compile('TTL=\d*')
            try: 
                sistema_operativo: str = pattern.search(str(res)).group()
                if sistema_operativo[4:] == "128":
                    sistema_operativo = "windows"
                else:
                    sistema_operativo = "linux"

                yield {
                    'status': 'online',
                    'dispositivo': getfqdn(ip),
                    "sistema_operativo": sistema_operativo,
                    "ip": ip
                }
            except:
                print("No se ha podido establecer conexión")
                print("Ip: {}".format(ip))
            
