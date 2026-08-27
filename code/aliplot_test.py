from sugar import read

# seqs = read('https://osf.io/download/j2wyv')
# for seq in seqs:
#     seq.id = seq.id.split('-')[-1]
# seqs.write('eve_in_bats.fasta')
# seqs2 = seqs[:10, :150].copy()
# seqs2.write('eve_in_bats_subset.fasta')

seqs = read('eve_in_bats.fasta')
seqs.plot_alignment('eve_in_bats.png', aspect=2)
aa = seqs.copy().translate(complete=True)
aa.plot_alignment('eve_in_bats_aa.png', aspect=2)

seqs2 = read('eve_in_bats_subset.fasta')
seqs2.plot_alignment('eve_in_bats_subset.png', aspect=2)
seqs2.copy().translate(complete=True).plot_alignment(

    'eve_in_bats_aa_subset.png', #color='flower',
    show=True,
    aspect=None)

