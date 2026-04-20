import flet as ft

def LoginView(page: ft.Page, auth_controller):
    # Campos de entrada
    email_input = ft.TextField(
        label="Correo electrónico",
        width=350,
        border_radius=10,
        keyboard_type=ft.KeyboardType.EMAIL
    )
    
    pass_input = ft.TextField(
        label="Contraseña",
        password=True,
        can_reveal_password=True,
        width=350,
        border_radius=10
    )

    def login_click(e):
        # Validación de campos vacíos
        if not email_input.value or not pass_input.value:
            page.snack_bar = ft.SnackBar(ft.Text("Por favor, llene todos los campos"))
            page.snack_bar.open = True
            page.update()
            return

        # Llamada al controlador
        user, msg = auth_controller.login(email_input.value, pass_input.value)

        if user:
            page.session.set("user", user)
            page.go("/dashboard")
        else:
            page.snack_bar = ft.SnackBar(ft.Text(msg))
            page.snack_bar.open = True
            page.update()

    # Botón de entrada
    login_button = ft.ElevatedButton(
        "Entrar",
        on_click=login_click,
        width=350,
        bgcolor="blue",
        color="white"
    )

    # Permitir entrar al presionar "Enter" en la contraseña
    pass_input.on_submit = login_click

    return ft.View(
        route="/",
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        appbar=ft.AppBar(
            title=ft.Text("SIGE - Login"),
            bgcolor="bluegrey900",
            color="white"
        ),
        controls=[
            ft.Column(
                [
                    ft.Text("Acceso al Sistema", size=24, weight="bold"),
                    email_input,
                    pass_input,
                    login_button,
                    ft.TextButton(
                        "Crear una cuenta nueva",
                        on_click=lambda _: page.go("/registro")
                    )
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                tight=True,
                spacing=20
            )
        ]
    )