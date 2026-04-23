class AuthController:

    def __init__(self):

        pass

   

    def login(self, email, password):

        # Simulación de BD: las llaves deben coincidir con lo que usa el Dashboard

        if email == "admin@gmail.com" and password == "1234":

            user = {

                "id_usuario": 1,

                "email": email,

                "nombre": "Administrador",

                "role": "admin"

            }

            return user, "Login exitoso"

        else:

            return None, "Correo o contraseña incorrectos"