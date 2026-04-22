import flet as ft 
from controllers.UserController import AuthController
from controllers.TareaController import TareaController
from views.LoginView import LoginView
from views.DashboardView import DashboardView
from views.RegistroView import RegistroView # Asegúrate de tener este import

def start(page: ft.Page):
    # Configuración inicial de la página
    page.title = "Sistema SIGE"
    page.window_width = 450
    page.window_height = 700

    # Inicializamos controladores
    auth_ctrl = AuthController()
    task_ctrl = TareaController()

    def route_change(e):
        # Limpiamos las vistas actuales para evitar duplicados
        page.views.clear()
        
        # Caso 1: Login
        if page.route == "/":
            page.views.append(LoginView(page, auth_ctrl))
        
        # Caso 2: Dashboard
        elif page.route == "/dashboard":
            page.views.append(DashboardView(page, task_ctrl))

        page.update()

    def view_pop(e):
        if len(page.views) > 1:
            page.views.pop()
            top_view = page.views[-1]
            page.go(top_view.route)

    # 1. Asignar los manejadores de eventos primero
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    # 2. IMPORTANTE: No fuerces page.route = "". Usa directamente page.go()
    print("Iniciando navegación...")
    if page.route == "/":
        route_change(None)
    else:
        page.go("/")

def main():
    # Es recomendable usar el puerto o modo web si hay problemas de renderizado
    ft.app(target=start)

if __name__ == "__main__":
    main()