# -*- coding: utf-8 -*-
#Created by Kenny William Nyallau 2020
from dnautil import constant

class DNAUtils:
    def __init__(self, dna):
        super().__init__()
        self.dna = dna

    def has_stop_codon(self, frame: int) -> bool:
        stop_codon_found = False
        for i in range(frame, len(self.dna), 3):
            codon = self.dna[i:i+3].lower()
            if codon in constant.STOP_CODONS:
                stop_codon_found = True
                break
        return stop_codon_found
    
    def transcribe(self) -> str:
        dna = list(self.dna)
        t_rna = list()
        for i in range(len(dna)):
            if dna[i] == 'T':
                t_rna.append('U')
            else:
                t_rna.append(dna[i])
        result = ''.join(t_rna)
        return result

    def complement(self) -> str:
        self.letters = ''
        self.letters = list(self.dna)
        self.letters = [constant.BASE_COMPLEMENT[base] for base in self.letters]
        return ''.join(self.letters)
    
    def reverse_complement(self) -> str:
        complement_bases = self.complement()
        reversed_complements = list(complement_bases)
        return ''.join(reversed_complements[::-1])