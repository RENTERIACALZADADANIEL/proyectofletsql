import bcrypt
from .databaseModel import Database

class UsuarioModel:
    def __init__(self):
        self.db = Database()
        
    def registrar(self,usuario_data):
        salt=bcrypt.gensalt()
        hashed_pw= bcrypt.hashpw(usuario_data.password.encode('utf-8'),salt)
        
        conn=self.db.get_connection()
        cursor=conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO usuarios (nombre,email,password) VALUES (%s , %s , %s)",
                (usuario_data.nombre, usuario_data.email, hashed_pw.decode('utf-8'))
            )
            conn.commit()
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False
        finally:
            conn.close()
        
    def validar_login(self,email,password):
        conn= self.db.get_connection()
        cursor=conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM usuarios WHERE email=%s",(email,))
        user = cursor.fetchone()
        conn.close()
        
        if user and bcrypt.checkpw(password.encode('utf-8'),user['password'].encode('utf-8')):
            return user
        return None
        