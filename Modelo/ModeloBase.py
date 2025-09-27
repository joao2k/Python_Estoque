import mysql.connector
import config
from libraries import Util
class DB:
    def __init__(self):
        self.cfg = config.Config()

    def _conectar(self):
        try :
            conn = mysql.connector.connect(
                host=self.cfg.get_ip(),
                user=self.cfg.get_usuario(),
                password=self.cfg.get_senha(),
                database=self.cfg.get_db()
            )
            cursor = conn.cursor(dictionary=True)
            return conn, cursor
        except Exception as e:
            cursor.close()
            conn.close()
            Util.registrar_erro(e)
            return None, None

    def select(self, query, atributos=None):
        try:
            if atributos is not None and not isinstance(atributos, (list, tuple)):
                atributos = (atributos,)
            conn, cursor = self._conectar()
            if not conn or not cursor:
                return "ERRO"
            cursor.execute(query, atributos)
            resultado = cursor.fetchall()
            cursor.close()
            conn.close()
            return resultado
        except Exception as e:
            cursor.close()
            conn.close()
            Util.registrar_erro(e)
            return "ERRO"


    def insert(self, query, atributos=None):
        try:
            if atributos is not None and not isinstance(atributos, (list, tuple)):
                atributos = (atributos,)
            conn, cursor = self._conectar()
            if not conn or not cursor:
                return "ERRO"
            cursor.execute(query, atributos)
            conn.commit()
            last_id = cursor.lastrowid
            cursor.close()
            conn.close()
            return last_id
        except Exception as e :
            cursor.close()
            conn.close()
            Util.registrar_erro(e)
            return "ERRO"

    def update(self, query, atributos=None):
        try:
            if atributos is not None and not isinstance(atributos, (list, tuple)):
                atributos = (atributos,)
            conn, cursor = self._conectar()
            if not conn or not cursor:
                return "ERRO"
            cursor.execute(query, atributos)
            conn.commit()
            linhas_afetadas = cursor.rowcount
            cursor.close()
            conn.close()
            return linhas_afetadas
        except Exception as e:
            cursor.close()
            conn.close()
            Util.registrar_erro(e)
            return "ERRO"
    def delete(self, query, atributos=None):
        try:
            if atributos is not None and not isinstance(atributos, (list, tuple)):
                atributos = (atributos,)
            conn, cursor = self._conectar()
            if not conn or not cursor:
                return "ERRO"
            cursor.execute(query, atributos)
            conn.commit()
            linhas_afetadas = cursor.rowcount
            cursor.close()
            conn.close()
            return linhas_afetadas
        except Exception as e:
            cursor.close()
            conn.close()
            Util.registrar_erro(e)
            return "ERRO"
