from fasta import fastautil as fst
from miscutil.util import *
from Bio import SeqIO
import os

cur_path = os.getcwd()

def main():
    data = 'data/dna2.fasta'
    datapath = os.path.join(cur_path, data)
    genotest = fst.FastaUtils(datapath)
    #records_len, record_seqs, record_ids, record_counts, \
    dict_id_seqs  = genotest.get_fasta_record_info()
    genotest.ORF_finder(dict_id_seqs)

if __name__ == "__main__":
    main()