import flet as ft

def LoginView(page: ft.Page, auth_controller):
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
        if not email_input.value or not pass_input.value:
            page.snack_bar = ft.SnackBar(ft.Text("Por favor, llene todos los campos"))
            page.snack_bar.open = True
            page.update()
            return

        user, msg = auth_controller.login(email_input.value, pass_input.value)

        if user:
            page.session.set("user", user)
            page.go("/dashboard")
        else:
            # Aquí mostrará si el correo no existe o si la contraseña está mal
            page.snack_bar = ft.SnackBar(ft.Text(msg))
            page.snack_bar.open = True
            page.update()

    return ft.View(
        route="/",
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        appbar=ft.AppBar(title=ft.Text("SIGE - Login"), bgcolor="bluegrey900", color="white"),
        controls=[
            ft.Column(
                [
                    ft.Icon(ft.Icons.LOCK_PERSON, size=50, color="blue"),
                    ft.Text("Acceso al Sistema", size=24, weight="bold"),
                    email_input,
                    pass_input,
                    ft.ElevatedButton("Entrar", on_click=login_click, width=350, bgcolor="blue", color="white"),
                    ft.Row([
                        ft.TextButton("¿Olvidaste tu contraseña?", on_click=lambda _: print("Recuperar")),
                        ft.TextButton("Crear cuenta", on_click=lambda _: page.go("/registro")),
                    ], alignment=ft.MainAxisAlignment.CENTER)
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=15
            )
        ]
    )