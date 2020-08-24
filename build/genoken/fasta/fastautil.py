# -*- coding: utf-8 -*-
#Created by Kenny William Nyallau 2020

from miscutil.util import Generate_Dictionary
from Bio.Blast import NCBIWWW, NCBIXML
from Bio import SeqIO
import re

class FastaUtils:
    def __init__(self, file):
        super().__init__()
        self.path = file
        self.blast_record = ''
        self.fasta_string = ''
        self.result_handle = ''
    
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

    def get_fasta_record_info(self):
        '''
        This will generate cleaner info on the fasta records
        '''
        ls_records_len = set()
        ls_record_id = list()
        ls_record_seqs = list()
        dict_id_seqs = Generate_Dictionary()
        record_count = 0
        
        for record in SeqIO.parse(self.path, "fasta"):
            ls_records_len.add(len(record))
            ls_record_id.append(record.id)
            dict_id_seqs.add(record.id, str(record.seq))
            ls_record_seqs.append(str(record.seq))
            record_count+=1
            
        print(f"List of records lengths: {ls_records_len}")
        print(f"Record count: {record_count}")
        return ls_records_len, ls_record_seqs, ls_record_id, record_count, dict_id_seqs

    def get_repr_multifasta_record(self):
        for seq_record in SeqIO.parse(self.path, "fasta"):
            print(repr(seq_record.seq))
            print(f"Sequence length: {len(seq_record)}")

    #Another method to get sequences from fasta record
    def get_each_sequence_from_fasta_record(self):
        seqs = dict()
        all_seqs = set()
        f = open(self.path)
        for line in f:
            line = line.rstrip()
            if line[0] == '>':
                words = line.split()
                name = words[0][:-1]
                seqs[name] = ''
            else:
                seqs[name] = seqs[name] + line
                all_seqs.add(seqs[name])
        return all_seqs
    
    def get_multifasta_record_count_and_len(self):
        count = 0
        record_len = set()
        for record in SeqIO.parse(self.path, "fasta"):
            count +=1
            record_len.add(len(record))
        return count, record_len
    
    def max_sequence_len(self, seq_len):
        return max(seq_len)
    
    def min_sequence_len(self, seq_len):
        return min(seq_len)
    
    def ORF_finder(self, dict_id_seqs):
        for seq_id, seq in dict_id_seqs.items():
            pattern = re.compile(r'(?=(ATG(?:...)*?)(?=TAG|TGA|TAA))', re.I)
            match = pattern.findall(seq)
            start = match.start()
            end = match.end()
            print(seq_id)
            print(seq)