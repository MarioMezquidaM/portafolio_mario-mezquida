import reflex as rx
from portafolio_mario.components.heading import heading


def about(description: str) -> rx.Component:
    return rx.vstack(
        heading("Sobre mí"),
        rx.text(description)
    )
