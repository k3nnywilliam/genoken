# -*- coding: utf-8 -*-
#Created by Kenny William Nyallau 2020
import constant

class DNAUtils:
    def __init__(self, dna):
        super().__init__()
        self.dna = dna
        self.letters = ''

    def has_stop_codon(self, stop_codons, frame=0):
        stop_codon_found = False
        
        for i in range(frame, len(self.dna), 3):
            codon = self.dna[i:i+3].lower()
            if codon in constant.STOP_CODONS:
                stop_codon_found = True
                break
        return stop_codon_found
    
    def transcribe(self):
        my_rna = list(self.dna)
        t_rna = []
        
        for i in range(len(my_rna)):
            if 'T' in my_rna:
                t_rna.append('U')
            else:
                t_rna.append(my_rna[i])
        return t_rna
    
    def complement(self):
        self.letters = list(self.dna)
        self.letters = [constant.BASE_COMPLEMENT[base] for base in self.letters]
        return ''.join(self.letters)

    def reverse_complement(self):
        complement_bases = self.complement()
        reversed_complements = list(complement_bases)
        return ''.join(reversed_complements[::-1])