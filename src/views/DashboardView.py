import flet as ft

def DashboardView(page, tarea_controller):
    user = page.session.get("user")
    
    lista_tareas = ft.Column(scroll=ft.ScrollMode.ALWAYS, expand=True)
    search_results = ft.Column(scroll=ft.ScrollMode.ALWAYS, expand=True)
    txt_titulo = ft.TextField(label="Nueva Tarea rápida", expand=True)

    def refresh_home():
        lista_tareas.controls.clear()
        tareas = tarea_controller.obtener_lista(user['id_usuario'])
        for t in tareas:
            lista_tareas.controls.append(
                ft.Card(ft.Container(content=ft.ListTile(
                    title=ft.Text(t['titulo'], weight="bold"),
                    subtitle=ft.Text(f"{t['descripcion']}\nPrioridad: {t['prioridad']}"),
                    trailing=ft.Badge(content=ft.Text(t['estado']), bgcolor=ft.Colors.BLUE_GREY_700)
                ), padding=10))
            )
        page.update()

    def search_tasks(e):
        query = e.control.value.lower()
        search_results.controls.clear()
        if query:
            tareas = tarea_controller.obtener_lista(user['id_usuario'])
            for t in tareas:
                if query in t['titulo'].lower() or (t['descripcion'] and query in t['descripcion'].lower()):
                    search_results.controls.append(
                        ft.ListTile(
                            title=ft.Text(t['titulo']),
                            subtitle=ft.Text(f"Estado: {t['estado']}"),
                            leading=ft.Icon(ft.Icons.TASK_ALT)
                        )
                    )
        page.update()

    # --- CONTENIDOS POR PESTAÑA ---
    home_view = ft.Column([
        ft.Row([txt_titulo, ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=lambda _: (tarea_controller.guardar_nueva(user['id_usuario'], txt_titulo.value, "", "media", "personal"), refresh_home()))]),
        ft.Text("Mis Tareas", size=20, weight="bold"),
        lista_tareas
    ], expand=True)

    search_view = ft.Column([
        ft.Text("Buscar en mis tareas", size=20, weight="bold"),
        ft.TextField(label="Escribe el nombre...", prefix_icon=ft.Icons.SEARCH, on_change=search_tasks),
        search_results
    ], visible=False, expand=True)

    settings_view = ft.Column([
        ft.Container(height=20),
        ft.CircleAvatar(content=ft.Text(user['nombre'][0].upper()), radius=40, bgcolor="blue"),
        ft.Text(f"{user['nombre']} {user.get('apellido', '')}", size=24, weight="bold"),
        ft.Divider(),
        ft.ListTile(leading=ft.Icon(ft.Icons.EMAIL), title=ft.Text("Correo"), subtitle=ft.Text(user['email'])),
        ft.ListTile(leading=ft.Icon(ft.Icons.PHONE), title=ft.Text("Teléfono"), subtitle=ft.Text(user.get('telefono', 'No asignado'))),
        ft.ElevatedButton("Cerrar Sesión", icon=ft.Icons.LOGOUT, on_click=lambda _: page.go("/"), color="red")
    ], visible=False, horizontal_alignment=ft.CrossAxisAlignment.CENTER)

    content_container = ft.Container(content=home_view, expand=True, padding=20)

    def nav_change(e):
        idx = e.control.selected_index
        home_view.visible = (idx == 0)
        search_view.visible = (idx == 1)
        settings_view.visible = (idx == 2)
        content_container.content = home_view if idx == 0 else search_view if idx == 1 else settings_view
        if idx == 0: refresh_home()
        page.update()

    return ft.View(
        "/dashboard",
        controls=[
            ft.AppBar(title=ft.Text("SIGE - Dashboard"), bgcolor="bluegrey900", color="white"),
            content_container
        ],
        navigation_bar=ft.NavigationBar(
            destinations=[
                ft.NavigationDestination(icon=ft.Icons.HOME_OUTLINED, selected_icon=ft.Icons.HOME, label="Inicio"),
                ft.NavigationDestination(icon=ft.Icons.SEARCH, label="Buscar"),
                ft.NavigationDestination(icon=ft.Icons.PERSON_OUTLINED, selected_icon=ft.Icons.PERSON, label="Perfil"),
            ],
            on_change=nav_change
        ),
        on_open=lambda _: refresh_home()
    )