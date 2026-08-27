import io

import matplotlib.pyplot as plt
from nicegui import run, ui
from sugar import FeatureList


def savefig_to_bytes(fig, **kwargs):
    buf = io.BytesIO()
    fig.savefig(buf, **kwargs)
    return buf.getvalue()


def plot_nextgene(gois, genes, range=100_000):
    gois = FeatureList.fromfmtstr(gois)
    genes = FeatureList.fromfmtstr(genes)
    plot_genes = FeatureList()
    for i, goi in enumerate(gois):
        add_genes = genes.select(seqid=goi.seqid).slice(start=goi.locs.start-range, stop=goi.locs.stop+range)
        add_genes.append(goi)
        for ft in add_genes:
            ft.meta.group = i
        plot_genes.extend(add_genes)
    fig = plot_genes.plot_ftsviewer(groupby='group', axlabel='{seqid}', align=gois, align_strand='+',
                                    crop=True, colorby='name', sharex=True)
    bytes = savefig_to_bytes(fig)
    plt.close(fig)
    return bytes


@ui.page('/')
def main_page():

    state = {'gois': None,
             'genes': None}

    async def handle_upload(event, key):
        content = await event.file.read()
        try:
            fts = FeatureList.fromfmtstr(content)
            state[key] = content
        except Exception as ex:
            ui.notify(f'Could not process uploaded file: {ex}', type='negative')
            state[key] = None
            download_button.disable()
        else:
            if state['gois'] is not None and state['genes'] is not None:
                download_button.enable()

    async def download_plot():
        spinner.set_visibility(True)
        fmt = outformat.value
        bytes = await run.cpu_bound(plot_nextgene, state['gois'], state['genes'], range=int(10 ** slider.value))
        ui.download.content(bytes, filename=f'nextgene_plot.{fmt.lower()}')
        spinner.set_visibility(False)

    with ui.column().classes('w-full items-center'):
        ui.label('NextGene Plotter').classes('text-2xl font-bold')
        ui.upload(
            label='Upload Genes Of Interest file',
            on_upload=lambda event: handle_upload(event, 'gois'),
            auto_upload=True,
        )
        ui.upload(
            label='Upload Genes file',
            on_upload=lambda event: handle_upload(event, 'genes'),
            auto_upload=True,
        )
        label = ui.label()
        slider = ui.slider(min=2, max=9, value=5, step=0.2).style('width: 300px')
        label.bind_text_from(slider, 'value', lambda value: f'Range: {int(10**value):,d}')
        with ui.row().classes('items-center gap-6'):
            outformat = ui.select(['PNG', 'PDF', 'SVG'], value='PNG')
            download_button = ui.button('Download plot', on_click=download_plot)
            spinner = ui.spinner()
            spinner.set_visibility(False)
        download_button.disable()


ui.run(title='NextGene Plotter')
