from sugar import read_fts, FeatureList

# a)
hits = read_fts('../data/hok/*_results.tab')
hits.write('../output/hok_hits.gff')

# b)
fts = read_fts('../data/hok/genomes/*/*.gff')
genes = fts.select('gene')
genes.write('../output/hok_genes.gff')

# c)
gois = read_fts('../output/hok_hits.gff')
genes = read_fts('../output/hok_genes.gff')
plot_genes = FeatureList()
# d)
locrange = 1000
for i, goi in enumerate(gois):
    add_genes = genes.select(seqid=goi.seqid).slice(start=goi.loc.start-locrange, stop=goi.loc.stop+locrange)
    add_genes.append(goi)
    for ft in add_genes:
        ft.meta.group = i
    plot_genes.extend(add_genes)

# e)
plot_genes.plot_ftsviewer(fname='../output/hok_nextgenes.pdf', groupby='group',
                          axlabel='{seqid}', colorby='name',
                          align=gois, align_strand='+',
                          crop=0, sharex=True)

