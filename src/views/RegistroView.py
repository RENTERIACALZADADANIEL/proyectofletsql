import flet as ft

def RegistroView(page: ft.Page, auth_controller):
    nombre = ft.TextField(label="Nombre", width=350)
    apellido = ft.TextField(label="Apellido", width=350)
    email = ft.TextField(label="Correo electrónico", width=350)
    password = ft.TextField(label="Contraseña", password=True, can_reveal_password=True, width=350)
    telefono = ft.TextField(label="Teléfono", width=350)

    def registrar_click(e):
        if not nombre.value or not email.value or not password.value:
            page.snack_bar = ft.SnackBar(ft.Text("Completa los campos obligatorios"))
            page.snack_bar.open = True
            page.update()
            return

        exito, msg = auth_controller.registrar_usuario(
            nombre.value, apellido.value, email.value, password.value, telefono.value
        )

        if exito:
            page.snack_bar = ft.SnackBar(ft.Text("¡Usuario creado! Inicia sesión"))
            page.snack_bar.open = True
            page.go("/")
        else:
            page.snack_bar = ft.SnackBar(ft.Text(msg))
            page.snack_bar.open = True
        page.update()

    return ft.View(
        "/registro",
        controls=[
            ft.AppBar(title=ft.Text("Registro de Usuario"), bgcolor="bluegrey900"),
            ft.Column([
                ft.Text("Crea tu cuenta", size=25, weight="bold"),
                nombre, apellido, email, password, telefono,
                ft.ElevatedButton("Registrar", on_click=registrar_click, bgcolor="blue", color="white", width=350),
                ft.TextButton("Volver al Login", on_click=lambda _: page.go("/"))
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=15)
        ],
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )