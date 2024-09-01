import reflex as rx

from rxconfig import config


class State(rx.State):
    """The app state."""

    theme_mode: str = "light"
    
    def toggle_theme(self):
        """Toggle between light and dark theme."""
        self.theme_mode = "dark" if self.theme_mode == "light" else "light"


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Welcome to Reflex!", size="9", color="blue"),  # Color del encabezado
            rx.text(
                "Get started by editing ",
                rx.code("Mario Mezquida", color="green"),  # Color del texto en código
                size="5",
                color="purple"  # Color del texto
            ),
            rx.link(
                rx.button("Check out our docs!", color="white", bg="blue"),  # Color del botón y fondo
                href="https://reflex.dev/docs/getting-started/introduction/",
                is_external=True,
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.logo(),
    )


app = rx.App()
app.add_page(index)
