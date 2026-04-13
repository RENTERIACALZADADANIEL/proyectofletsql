import flet as ft

def DashboardView(page, tarea_controller):
    user = page.session.get("user")
    lista_tareas = ft.Column(scroll=ft.ScrollMode.ALWAYS, expand=True)

    def refresh():
        lista_tareas.controls.clear()
        # Obtenemos las tareas desde el controlador usando el ID del usuario en sesión
        for t in tarea_controller.obtener_lista(user['id_usuario']):
            lista_tareas.controls.append(
                ft.Card(
                    content=ft.Container(
                        content=ft.ListTile(
                            title=ft.Text(t['titulo'], weight="bold"),
                            subtitle=ft.Text(f"{t['descripcion']}\nPrioridad: {t['prioridad']}"),
                            trailing=ft.Badge(content=ft.Text(t['estado']), bgcolor=ft.Colors.ORANGE_300)
                        ), padding=10
                    )
                )
            )
        page.update()

    # Formulario rápido para nueva tarea
    txt_titulo = ft.TextField(label="Nueva Tarea", expand=True)

    def add_task(e):
        # Valores por defecto para descripción, prioridad y clasificación
        success, msg = tarea_controller.guardar_nueva(
            user['id_usuario'], 
            txt_titulo.value, 
            "", 
            "media", 
            "trabajo"
        )
        if success:
            txt_titulo.value = ""
            refresh()

    return ft.View("/dashboard", [
        ft.AppBar(
            title=ft.Text(f"Bienvenido, {user['nombre']}"),
            actions=[
                ft.IconButton(ft.Icons.EXIT_TO_APP, on_click=lambda _: page.go("/"))
            ],
        ),
        ft.Column([
            ft.Row([
                txt_titulo,
                ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=add_task),
            ]),
            ft.Divider(),
            ft.Text("Mis Tareas Pendientes", size=20, weight="bold"),
            lista_tareas
        ], expand=True, padding=20),
    ], on_open=lambda _: refresh())