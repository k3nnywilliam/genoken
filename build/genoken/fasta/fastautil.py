# -*- coding: utf-8 -*-
#Created by Kenny William Nyallau 2020

from miscutil.util import Generate_Dictionary, GenokenUtils
from dnautil import constant
from Bio.Blast import NCBIWWW, NCBIXML
from Bio import SeqIO, Seq
import re

class FastaUtils:
    def __init__(self, filepath):
        super().__init__()
        self.path = filepath
        self.blast_record = ''
        self.fasta_string = ''
        self.result_handle = ''
        self.seq_len = 0
        self.record_count = 0
        self.ls_records_len = set()
        self.ls_record_id = list()
        self.ls_record_seqs = list()
        self.dict_id_seqs = Generate_Dictionary()
    
    @GenokenUtils.timer_logging
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
    
    @GenokenUtils.timer_logging
    def get_fasta_record_info(self):
        '''
        This will generate various info of the fasta records
        '''
        self.record_count = 0
        
        for record in SeqIO.parse(self.path, "fasta"):
            #print(f"Repr: {repr(record.seq)}")
            self.ls_records_len.add(len(record))
            self.ls_record_id.append(record.id)
            self.dict_id_seqs.add(record.id, str(record.seq))
            self.ls_record_seqs.append(str(record.seq))
            self.record_count+=1
        print(f"Record count: {self.record_count}")
        print(f"Longest sequence in file: {max(self.ls_records_len)}")
        print(f"Shortest sequence in file: {min(self.ls_records_len)}")
        return self.ls_records_len, self.ls_record_seqs, self.ls_record_id, self.record_count, self.dict_id_seqs
    
    
    def start_ORF_finder_example(self, frame=0):
        mylist = list()
        for seq_id, seq in self.dict_id_seqs.items():
            for orflen, orf in self.simple_ORF_finder(seq, frame):
                mylist.append(orflen)
        print(sorted(mylist))
    
    def simple_ORF_finder_example(self, seq, frame):
        for i in range(frame, len(seq), 3):
            codon1 = seq[i:i+3]
            if codon1 == 'ATG':
                position1 = i
                for j in range(position1, len(seq), 3):
                    codon2 = seq[j:j+3]
                    if codon2 in constant.STOP_CODONS:
                        position2 = j
                        yield (position2-position1+3, seq[position1:position2+3])
                        break
    
    def orf_tester(self, frame=0):
        for seq_id, seq in self.dict_id_seqs.items():
            self.find_ORF(seq, frame)

    def find_ORF(self, seq, frame=0):
        start_pos = 0
        stop_pos = 0
        
        for i in range(frame, len(seq), 3):
            start=seq[i:i+3]
            if start in constant.START_CODON:
                start_pos = i
                break
            for j in range(i+1, len(seq) - 1, 3):
                stop = seq[j:j+3]
                #print(stop)
                if stop in constant.STOP_CODONS:
                    stop_pos = j
        print(f"longest orf length {stop_pos - start_pos+3}")
    