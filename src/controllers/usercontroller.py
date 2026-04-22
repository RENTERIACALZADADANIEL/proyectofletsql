from models.UserModel import UsuarioModel
from models.schemasModel import UsuarioSchema
from pydantic import ValidationError

class AuthController:
    def __init__(self):
        self.model = UsuarioModel()

    def login(self, email, password):
        # 1. Buscar si el correo existe
        user = self.model.buscar_por_email(email)
        
        if not user:
            return None, "El correo electrónico no existe"
        
        # 2. Validar la contraseña
        login_valido = self.model.validar_login(email, password)
        
        if not login_valido:
            return None, "La contraseña es incorrecta"
            
        return login_valido, "Éxito"

    def registrar_usuario(self, nombre, email, password):
        try:
            nuevo_usuario = UsuarioSchema(nombre=nombre, email=email, password=password)
            success = self.model.registrar(nuevo_usuario)
            return success, "Usuario creado correctamente"
        except ValidationError as e:
            return False, e.errors()[0]['msg']