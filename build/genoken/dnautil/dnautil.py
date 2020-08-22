# -*- coding: utf-8 -*-
#Created by Kenny William Nyallau 2020
from Bio.Seq import Seq

class DNAUtils:
    def __init__(self, dna):
        super().__init__()
        self.dna = dna

    def has_stop_codon(self, stop_codons, frame=0):
        stop_codon_found = False
        stop_codons = ['tga', 'tag', 'taa']
        
        for i in range(frame, len(self.dna), 3):
            codon = self.dna[i:i+3].lower()
            if codon in stop_codons:
                stop_codon_found = True
                break
        return stop_codon_found

    def complement(self):
        base_complement = {'A':'T', 'C': 'G', 'G':'C', 'T':'A', 'N':'N'}
        letters = list(self.dna)
        letters = [base_complement[base] for base in letters]
        return ''.join(letters) 
    
    def transcribe(self):
        my_rna = list(self.dna)
        t_rna = []
        
        for i in range(len(my_rna)):
            if 'T' in my_rna:
                t_rna.append('U')
            elif 't' in my_rna:
                t_rna.append('u')
            else:
                t_rna.append(my_rna[i])
        return t_rna
                
    def reverse_complement(self):
        rc_dna = list(self.dna)
        return rc_dna[::-1]