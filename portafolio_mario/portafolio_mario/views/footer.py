import reflex as rx
from portafolio_mario.components.media import media
from portafolio_mario.data import Media
from portafolio_mario.styles.styles import Size


def footer(data: Media) -> rx.Component:
    return rx.vstack(
        rx.text("Nombre"),
        media(data),
        spacing=Size.SMALL.value
    )
