Query file:				query_hok.fasta
BLAST/MMSeqs2 output:	*_results.tab
Genomes:				genomes/*/*.fna
GFF files for genomes:	genomes/*/*.gff


# Genomes
https://www.ncbi.nlm.nih.gov/datasets/taxonomy/511145/
https://www.ncbi.nlm.nih.gov/datasets/taxonomy/99287/

# Toxin protein hokA-D
https://d-lab.arna.cnrs.fr/display/display_feature_table/TA05974
https://d-lab.arna.cnrs.fr/display/display_feature_table/TA05971
https://d-lab.arna.cnrs.fr/display/display_feature_table/TA05972
https://d-lab.arna.cnrs.fr/display/display_feature_table/TA05700


# Search
mamba create -n gcb2026_prep -c conda-forge -c bioconda blast mmseqs2 -y
mamba activate gcb2026_prep

bash script/search.sh
