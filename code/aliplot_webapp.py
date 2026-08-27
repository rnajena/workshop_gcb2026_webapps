import io

from nicegui import ui
from sugar import BioBasket


def aliplot(content, fig, symbols=None, translate=False, color='default'):
    seqs = BioBasket.fromfmtstr(content)
    if translate:
        try:
            seqs.translate(complete=True)
        except Exception as ex:
            ui.notify(f'Could not translate sequences: {ex}', type='warning')
            return
    if color and color == 'default':
        color = None
    ax = fig.gca()
    ax.clear()
    return seqs.plot_alignment(ax=ax, symbols=symbols, color=color)


def savefig_to_bytes(fig, **kwargs):
    buf = io.BytesIO()
    fig.savefig(buf, **kwargs)
    return buf.getvalue()

COLORS = ['default', 'autumn', 'blossom', 'buried', 'clustalx', 'clustalx_nt', 'flower', 'hydrophobicity', 'ocean', 'prohelix', 'propstrand', 'propturn', 'rainbow', 'rainbow_nt', 'spring', 'sunset', 'taylor', 'wither', 'zappo']

@ui.page('/')
def main_page():
    state = {'upload': None}

    def update_plot():
        if state['upload'] is not None:
            with fig:
                aliplot(state['upload'], fig,
                        symbols=symbols_input.value,
                        translate=translate_input.value,
                        color=color_input.value
                        )

    async def handle_upload(event):
        content = await event.file.read()
        try:
            state['upload'] = content
            update_plot()
        except Exception as ex:
            ui.notify(f'Could not plot alignment: {ex}', type='negative')
            state['upload'] = None
        else:
            download_button.enable()

    def download_plot():
        fmt = outformat.value
        with fig:
            bytes = savefig_to_bytes(fig, format=fmt)
        ui.download.content(bytes, filename=f'alignment_plot.{fmt.lower()}')


    with ui.column().classes('w-full items-center'):
        ui.label('Alignment Viewer').classes('text-2xl font-bold')
        ui.upload(
            label='Upload alignment file',
            on_upload=handle_upload,
            auto_upload=True,
        )
        with ui.card():
            with ui.row().classes('items-center gap-6'):
                symbols_input = ui.switch(text='Show symbols', value=None, on_change=update_plot)
                translate_input = ui.switch(text='Translate', value=False, on_change=update_plot)
                color_input = ui.select(label='Color', options=COLORS, value='default', on_change=update_plot)
        with ui.matplotlib().figure as fig:
            pass
        with ui.row().classes('items-center gap-6'):
            outformat = ui.select(['PNG', 'PDF', 'SVG'], value='PNG')
            download_button = ui.button('Download plot', on_click=download_plot)
        download_button.disable()


ui.run(title='Alignment Viewer')

