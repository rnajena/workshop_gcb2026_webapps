# Code from the slides

from sugar import read

seqs = read('../data/NC_045512.2.gb')
print(seqs)
seqs2 = read('../data/AF086833.fasta')
print(seqs2)

seqs = read('../data/NC_045512.2.gb')
seqs2 = read('../data/AF086833.fasta')
print(seqs2[0].meta)
print(seqs[0].meta)

seqs = read('../data/NC_045512.2.gb')
first_cds = seqs['cds']
aa = first_cds.copy().translate()
print(aa)
aa.write('aa_first_cds.fasta')

seqs3 = read('../data/ali_pestivirus.stk')
print(seqs3[:3, 200:220])
seqs3.str.replace('-', '')
seqs3.write('pestivirus_original.fasta')

seqs3 = read('../data/ali_pestivirus_aa.clustal')
seqs3.plot_alignment(show=True)
seqs3.plot_alignment(fname='ali_pestivirus.png')
seqs3[-15:, 4000:4050].plot_alignment(show=True)
seqs3[-15:, 4000:4050].plot_alignment(fname='ali_pestivirus_subset.png')

from sugar import read_fts
fts = read_fts('../data/AF086833.gb')
print(fts[:6])
fts[:6].write('AF086833_test.gff')
fts_ia = read_fts('../data/influenza_a_blast.tsv')
seqs_ia = read('../data/influenza_a.fasta')
print(seqs_ia[fts_ia])

from sugar import read_fts
fts = read_fts('../data/AF086833.gb')
fts2 = fts.select('cds', len_ge=1000)
fts2.write('AF086833_long_cds.gff')

fts2.plot_ftsviewer(show=True)
fts2.plot_ftsviewer(fname='AF086833_long_cds.png')
