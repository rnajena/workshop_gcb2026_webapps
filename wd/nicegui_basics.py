# Code from a slide

from nicegui import ui

@ui.page('/')
def main():
    def greet(event):
        label.set_text(f"Hello {event.value}!")

    ui.label('Greeting').classes('text-2xl font-bold')
    with ui.row().classes('items-center'):
        ui.label('Please enter your name:')
        user_input = ui.input(on_change=greet)
    label = ui.label()

ui.run(main, title='Hello NiceGUI')
