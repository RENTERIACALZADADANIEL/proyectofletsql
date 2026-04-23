import flet as ft

def DashboardView(page, tarea_controller):
    user = getattr(page, "user_data", None)
    lista_tareas = ft.Column(scroll=ft.ScrollMode.ALWAYS, expand=True)

    def refresh():
        if user and 'id_usuario' in user:
            lista_tareas.controls.clear()
            tareas = tarea_controller.obtener_lista(user['id_usuario'])
            for t in tareas:
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

    txt_titulo = ft.TextField(label="Nueva Tarea", expand=True)

    def add_task(e):
        if user and 'id_usuario' in user:
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

    return ft.View(
        route="/dashboard", 
        controls=[
            ft.AppBar(
                title=ft.Text(f"Bienvenido, {user['nombre'] if user else 'Usuario'}"),
                actions=[
                    ft.IconButton(ft.Icons.EXIT_TO_APP, on_click=lambda _: page.go("/"))
                ],
            ),
            # CORRECCIÓN: Envolvemos la Columna en un Container para usar padding
            ft.Container(
                content=ft.Column([
                    ft.Row([
                        txt_titulo,
                        ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=add_task),
                    ]),
                    ft.Divider(),
                    ft.Text("Mis Tareas Pendientes", size=20, weight="bold"),
                    lista_tareas
                ], expand=True),
                padding=20, # Aquí es donde sí se permite el padding
                expand=True
            ),
        ]
    )