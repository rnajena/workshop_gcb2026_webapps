#!/usr/bin/env bash
set -e

# File Paths & Parameters
QUERY="query_hok.fasta"
MMSEQS_GENOME="genomes/GCF_000005845.2/GCF_000005845.2_ASM584v2_genomic.fna"
BLAST_GENOME="genomes/GCA_000006945.2/GCA_000006945.2_ASM694v2_genomic.fna"
OUT_DIR="."
MIN_BITSCORE=15

mkdir -p "$OUT_DIR/tmp_blast_db" "$OUT_DIR/tmp"

# 1. MMseqs2 Search + Bitscore Filter (Column 12 is bitscore)
mmseqs easy-search "$QUERY" "$MMSEQS_GENOME" "$OUT_DIR/mmseqs_raw.tab" "$OUT_DIR/tmp" --search-type 2
awk -v min_score="$MIN_BITSCORE" '$12 >= min_score' "$OUT_DIR/mmseqs_raw.tab" > "$OUT_DIR/mmseqs_results.tab"

# 2. BLAST Search + Bitscore Filter (Column 12 is bitscore)
makeblastdb -in "$BLAST_GENOME" -dbtype nucl -out "$OUT_DIR/blast_db/ASM694v2"
tblastn -query "$QUERY" -db "$OUT_DIR/blast_db/ASM694v2" -outfmt 6 | \
  awk -v min_score="$MIN_BITSCORE" '$12 >= min_score' > "$OUT_DIR/blast_results.tab"


rm -rf "$OUT_DIR/tmp" "$OUT_DIR/mmseqs_raw.tab" "$OUT_DIR/blast_db"

echo "Done! Filtered results (bitscore >= $MIN_BITSCORE) saved in $OUT_DIR"
