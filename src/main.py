import flet as ft
# Importación de Vistas
from views.LoginView import LoginView
from views.DashboardView import DashboardView
# Importación de Controladores
from controllers.UserController import AuthController
from controllers.TareaController import TareaController

def start(page: ft.Page):
    # Inicializamos los controladores
    auth_ctrl = AuthController()
    task_ctrl = TareaController()

    def route_change(e):
        page.views.clear()
        
        # Ruta de Login (Principal)
        if page.route == "/":
            page.views.append(LoginView(page, auth_ctrl))
        
        # Ruta de Dashboard
        elif page.route == "/dashboard":
            page.views.append(DashboardView(page, task_ctrl))

        # Caso de seguridad: Si algo falla, mostrar texto de error
        if not page.views:
            page.views.append(
                ft.View("/", [ft.Text("Error: Ruta no encontrada o vista vacía")])
            )
        
        page.update()

    # Configuración de la página
    page.on_route_change = route_change
    # Forzamos la navegación inicial
    page.go("/")

def main():
    # Ejecución de la app
    ft.app(target=start)

if __name__ == "__main__":
    main()