from .databaseModel import Database

class TareaModel:
    def __init__(self):
        self.db = Database()
    
    def listar_por_usuario(self,id_usuario):
        conn =self.db.get_connection()
        cursor= conn.cursor(dictionary=True)
        query =" SELECT * FROM tareas WHERE id_usuario = %s ORDER BY fecha_limite ASC"
        cursor.execute(query,(id_usuario,))
        resultado = cursor.fetchall()
        conn.close()
        return resultado
    
    def crear(self,id_usuario,titulo,descripcion,prioridad,clasificacion):
        conn=self.db.get_connection()
        cursor=conn.cursor()
        query= """INSERT INTO tareas(id_usuario,titulo,descripcion,prioridad,clasificacion)
                VALUES(%s , %s , %s , %s , %s)"""
        cursor.execute(query,(id_usuario,titulo,descripcion,prioridad,clasificacion))
        conn.commit()
        conn.close()