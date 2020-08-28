from dnautil import DNAUtils

dna = 'ATGATAGGCCTA'
du = DNAUtils(dna)
print(du.complement()) 
print(du.reverse_complement())