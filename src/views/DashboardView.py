import flet as ft

def DashboardView(page, tarea_controller):
    
    user = getattr(page, "user_data", None)
    
    lista_tareas = ft.Column(scroll=ft.ScrollMode.ALWAYS, expand=True)

    def refresh_tareas():
        if user and 'id_usuario' in user:
            lista_tareas.controls.clear()
            tareas = tarea_controller.obtener_lista(user['id_usuario'])
            for t in tareas:
                lista_tareas.controls.append(
                    ft.Card(
                        content=ft.Container(
                            content=ft.ListTile(
                                title=ft.Text(t['titulo'], weight="bold"),
                                subtitle=ft.Text(
                                    f"{t['descripcion']}\nPrioridad: {t['prioridad']}"
                                ),
                                trailing=ft.Container(
                                    content=ft.Text(t.get('estado', 'pendiente')),
                                    bgcolor=ft.Colors.ORANGE_300,
                                    padding=5,
                                    border_radius=5
                                )
                            ),
                            padding=10
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
                refresh_tareas()

    
    vista_inicio = ft.Column([
        ft.Row([
            txt_titulo,
            ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=add_task),
        ]),
        ft.Divider(),
        ft.Text("Mis Tareas Pendientes", size=20, weight="bold"),
        lista_tareas
    ], expand=True, visible=True) 

    
    vista_explorar = ft.Column([
        ft.Container(
            content=ft.Column([
                ft.Icon(ft.Icons.EXPLORE, size=50, color=ft.Colors.GREY_400),
                ft.Text("Próximamente...", size=20, color=ft.Colors.GREY_400),
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            alignment=ft.Alignment.CENTER,
            expand=True
        )
    ], expand=True, visible=False)

    
    vista_perfil = ft.Column([
        ft.Container(
            content=ft.Column([
                ft.CircleAvatar(
                    content=ft.Icon(ft.Icons.PERSON, size=40),
                    radius=40,
                    bgcolor=ft.Colors.BLUE_GREY_100
                ),
                ft.Text(user['nombre'] if user else "Usuario", size=24, weight="bold"),
                ft.Text(user['email'] if user else "correo@ejemplo.com", size=16, color=ft.Colors.GREY_700),
                ft.Text(f"Último acceso: {user.get('ultimo_acceso', 'Recién registrado')}" if user and user.get('ultimo_acceso') else "Último acceso: N/A", size=14, color=ft.Colors.GREY_500, italic=True),
                ft.Divider(height=40),
                
                ft.ListTile(
                    leading=ft.Icon(ft.Icons.SETTINGS),
                    title=ft.Text("Configuración"),
                    subtitle=ft.Text("Ajustes de la aplicación"),
                    on_click=lambda _: print("Configuración abierta")
                ),
                ft.ListTile(
                    leading=ft.Icon(ft.Icons.HELP_OUTLINE),
                    title=ft.Text("Ayuda y Soporte"),
                ),
                ft.Divider(),
                
                ft.ListTile(
                    leading=ft.Icon(ft.Icons.LOGOUT, color=ft.Colors.RED),
                    title=ft.Text("Cerrar Sesión", color=ft.Colors.RED, weight="bold"),
                    on_click=lambda _: page.go("/")
                ),
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            padding=20
        )
    ], expand=True, visible=False)

    
    def cambiar_pestana(e):
        idx = e.control.selected_index
        
        vista_inicio.visible = (idx == 0)
        vista_explorar.visible = (idx == 1)
        vista_perfil.visible = (idx == 2)
        
        if idx == 0:
            refresh_tareas()
            
        page.update()

    nav_bar = ft.NavigationBar(
        selected_index=0,
        on_change=cambiar_pestana,
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.HOME_OUTLINED, selected_icon=ft.Icons.HOME, label="Inicio"),
            ft.NavigationBarDestination(icon=ft.Icons.EXPLORE_OUTLINED, selected_icon=ft.Icons.EXPLORE, label="Explorar"),
            ft.NavigationBarDestination(icon=ft.Icons.PERSON_OUTLINE, selected_icon=ft.Icons.PERSON, label="Perfil"),
        ],
    )

    return ft.View(
        route="/dashboard",
        navigation_bar=nav_bar,
        controls=[
            ft.AppBar(
                title=ft.Text("SIGE"),
                bgcolor=ft.Colors.BLACK,
                color=ft.Colors.WHITE,
                automatically_imply_leading=False 
            ),
            ft.Container(
                content=ft.Stack([
                    vista_inicio,
                    vista_explorar,
                    vista_perfil
                ]),
                padding=20,
                expand=True
            ),
        ]
    )