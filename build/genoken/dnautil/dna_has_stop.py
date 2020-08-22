def has_stop_codon(dna, frame=0):
    stop_codon_found = False
    stop_codons = ['tga', 'tag', 'taa']
    
    for i in range(frame, len(dna), 3):
        codon = dna[i:i+3].lower()
        if codon in stop_codons:
            stop_codon_found = True
            break
    return stop_codon_found

def complement(dna):
    base_complement = {'A':'T', 'C': 'G', 'G':'C', 'T':'A', 'N':'N'}
    letters = list(dna)
    letters = [base_complement[base] for base in letters]
    return ''.join(letters)

dna = 'atgagcgcgcgat'
print(has_stop_codon(dna, 1))