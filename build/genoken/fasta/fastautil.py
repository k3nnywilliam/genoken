# -*- coding: utf-8 -*-
#!usr/bin/env python3
#Created by Kenny William Nyallau 2020

from misc.util import Generate_Dictionary, GenokenUtils
from dna import constant
from Bio.Blast import NCBIWWW, NCBIXML
from Bio import SeqIO, Seq
import re

class FastaUtils:
    def __init__(self, filepath):
        super().__init__()
        try:
            self.path = filepath
        except IOError:
            print(f"{self.path} cannot be opened.")
        self.result_handle = ''
        self.ls_records_len = set()
        self.ls_record_id = list()
        self.ls_record_seqs = list()
        self.dict_id_seqs = Generate_Dictionary()
    
    @GenokenUtils.timerlogging
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
        blast_record = NCBIXML.read(self.result_handle)
        print(f"Blast record alignments: {len(self.blast_record.aligments)}")
        return blast_record
    
    def get_fasta_record_info(self):
        """Returns a list of fasta file information

        Returns:
            list: Record lengths
            list: Record sequences
            list: Record ids
            list: Count of records
            dict: Key value pair of ids and sequences
        """
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
    
    def start_ORF_finder_example(self, frame=0) -> list:
        """Example of open reading frame 

        Args:
            frame (int, optional): Reading frame. Defaults to 0.

        Returns:
            list: lengths of ORF
        """
        mylist = list()
        for seq_id, seq in self.dict_id_seqs.items():
            for orflen, orf in self.simple_ORF_finder_example(seq, frame):
                mylist.append(orflen)
        print(sorted(mylist))
        return mylist
    
    def simple_ORF_finder_example(self, seq, frame=0):
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
            self.find_ORF(seq_id, seq, frame)

    def find_ORF(self, seq_id, seq, frame=0):
        start_pos = 0
        stop_pos = 0
        len_longest_orf = 0
        for i in range(frame, len(seq), 3):
            start=seq[i:i+3]
            if start in constant.START_CODON:
                start_pos = i
                break
            for j in range(i+1, len(seq) - 1, 3):
                stop = seq[j:j+3]
                if stop in constant.STOP_CODONS:
                    stop_pos = j
        len_longest_orf = stop_pos - start_pos+3
        result = {seq_id : len_longest_orf}
        print(f"Longest ORF length: {result}")
        return result
    