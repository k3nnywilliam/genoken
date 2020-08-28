from fasta import fastautil as fst
from miscutil.util import GenokenUtils
from Bio import SeqIO
import os

def main():
    DATA_DIR = os.path.join(os.path.abspath(os.curdir), 'data')
    genotest = fst.FastaUtils(os.path.join(DATA_DIR, 'dna2.fasta'))
    #records_len, record_seqs, record_ids, record_counts, \
    dict_id_seqs  = genotest.get_fasta_record_info()
    #genotest.start_ORF(frame=2)
    dna = "CCCATGCCCCCCCCCCCCCCCCCCCCCCCTAGCCCCCCCCTAATGATAG"
    genotest.orf_tester(2)
    #genotest.tester(dna)

if __name__ == "__main__":
    main()