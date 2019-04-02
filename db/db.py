from sqlite3 import connect, Connection, Cursor
from typing import List, Tuple


class Conexion:

    __nombre_base_de_datos: str = './db/db.db'
    __base_de_datos: Connection

    def __init__(self, commit: bool=True):
        """Constructor de la Clase, pasamos por parametro la opción commit (opcional)"""
        self.commit = commit

    def __enter__(self) -> Cursor:
        """Nos conectamos a la base de datos"""
        self.base_de_datos: Connection = connect(self.__nombre_base_de_datos)
        cursor: Cursor = self.base_de_datos.cursor()
        return cursor

    def __exit__(self, type: str, value: str, traceback: str) -> None:
        """Cerramos la conexión y guardamos"""
        if not traceback:
            if self.commit:
                self.base_de_datos.commit()
            self.base_de_datos.close()
        else:
            raise RuntimeError(traceback)
            return None


class Db:  

    def create_table(self) -> None:
        """Crea la base de datos, si existe no lo crea"""
        with Conexion() as cursor:
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Dispositivos(
                                ip TEXT NOT NULL,
                                active TEXT NOT NULL,
                                sistema_operativo TEXT NOT NULL,
                                nombre_dispositivo TEXT NOT NULL
                            );
            ''')

    def introducir_valores(self, ip: str, active: str, sistema_operativo: str, nombre_dispositivo: str) -> None:
        """Introduce valores directamente en la base de datos"""
        with Conexion() as cursor:
            cursor.execute('''
                INSERT INTO Dispositivos (
                    ip, active, sistema_operativo, nombre_dispositivo
                ) VALUES (
                    ?, ?, ?, ?
                )
            ''', [ip, active, sistema_operativo, nombre_dispositivo])

    def get_datos(self) -> List[Tuple[str]]:
        """Obtiene todos los datos, de la base de datos"""
        with Conexion(commit=False) as cursor:
            cursor.execute('''
                SELECT * FROM Dispositivos WHERE active='online'
            ''')
            datos: List[Tuple[str]] = cursor.fetchall()
        return datos

    def clear(self) -> None:
        """Elimina todos los Datos, de la base de datos"""
        with Conexion() as cursor:
            cursor.execute("""
                DELETE FROM Dispositivos
            """)
