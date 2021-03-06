# -*- coding: utf-8 -*-
#!usr/bin/env python3
#Created by Kenny William Nyallau 2020

from fasta.fastautil import FastaUtils
from misc.util import GenokenUtils
from Bio import SeqIO
import os

def main():
    DATA_DIR = os.path.join(os.path.abspath(os.curdir), 'data')
    genotest = FastaUtils(os.path.join(DATA_DIR, 'dna2.fasta'))
    #records_len, record_seqs, record_ids, record_counts, \
    dict_id_seqs  = genotest.get_fasta_record_info()
    #genotest.start_ORF(frame=2)
    dna = "CCCATGCCCCCCCCCCTCCCCACCCGCCCTAGCCCCCCCCTAATGATAG"
    genotest.orf_tester(2)
    #genotest.tester(dna)

if __name__ == "__main__":
    main()