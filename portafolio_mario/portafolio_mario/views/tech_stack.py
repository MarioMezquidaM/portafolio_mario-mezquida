import reflex as rx
from portafolio_mario.components.heading import heading
from portafolio_mario.data import Technology
from portafolio_mario.styles.styles import EmSize, Size


def tech_stack(technologies: list[Technology]) -> rx.Component:
    return rx.vstack(
        heading("Tecnologías"),
        rx.flex(
            *[
                rx.badge(
                    rx.box(
                        class_name=technology.icon,
                        font_size="24px"
                    ),
                    rx.text(technology.name),
                    size="2"
                )
                for technology in technologies
            ],
            wrap="wrap",
            spacing=Size.SMALL.value
        ),
        spacing=Size.DEFAULT.value
    )
