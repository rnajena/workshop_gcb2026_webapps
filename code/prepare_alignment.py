from sugar import read, read_fts

# a), b), c), d)
fts = read_fts('../data/hok/*_results.tab')
print(fts)
seqs = read('../data/hok/genomes/*/*.fna')
print(seqs[fts])
seqs[fts].write('../output/hok_hits.fasta')

# e)
# run in bash:
# mafft --auto ../output/hok_hits.fasta > ../output/hok_hits.aln

# f)
seqs2 = read('../output/hok_hits.aln')
seqs2.plot_alignment(aspect=2, fname='../output/ali_hok_hits.png')

# Bonus
seqs3 = read('../data/hok/query_hok.fasta')
for ft in fts:
    seq = seqs[ft][0]
    seq.id = seq.id + '_' + str(ft.locs.start)
    seqs3.append(seq.translate(complete=True))
seqs3.write('../output/hok_hits_aa.fasta')

# run in bash:
# mafft --auto ../output/hok_hits_aa.fasta > ../output/hok_hits_aa.aln

seqs4 = read('../output/hok_hits_aa.aln')
seqs4.plot_alignment(aspect=2, fname='../output/ali_hok_hits_aa.png', label=True,
                     #symbols=True, symbol_color='0.5'
                     )
