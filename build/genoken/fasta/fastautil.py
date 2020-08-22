# -*- coding: utf-8 -*-
#Created by Kenny William Nyallau 2020

from Bio.Blast import NCBIWWW, NCBIXML
from miscutil.util import *
import os

class FastaUtils:
    def __init__(self, file):
        super().__init__()
        self.path = str(os.getcwd())+file
        self.blast_record = ''
        self.fasta_string = ''
        self.result_handle = ''
    
    @timer_logging
    def init_blast_search(self):
        try:
            print(f"Fasta file: {self.path}")
            print("Searching through Blast database...")
            self.fasta_string = open(self.path).read()
            self.result_handle = NCBIWWW.qblast("blastn", "nt", self.fasta_string)
            print("Blast result handle ready.")
        except IOError:
            print(f"{self.path} cannot be opened.")
        
    def get_blast_record(self):
        self.blast_record = NCBIXML.read(self.result_handle)
        print(f"Blast record alignments: {len(self.blast_record.aligments)}")
        return self.blast_record
    
    def get_multifasta_record(self):
        pass
    
    def len_longest_sequence(self):
        pass
    
    def len_shortest_sequence(self):
        pass
    
    def ORF_len_longest(self, frame=0):
        pass
    
    def ORF_find_start_pos(self, frame=0):
        pass
    
    def ORF_find_longest_forward(self):
        pass
    
    def find_freq_repeats(self, len):
        pass
    
    def get_max_freq_repeats(self):
        pass
    
    def get_min_freq_repeats(self):
        pass
    
    