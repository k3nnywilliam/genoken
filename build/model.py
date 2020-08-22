from genoken.fasta import fastautil as fst

blast_search = fst.FastaUtils("/data/seq1.fa")
blast_search.init_blast_search()
#blast_search.get_fasta_record()