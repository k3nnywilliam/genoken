import unittest
from miscutil.util import GenokenUtils
from dnautil.dnautil import DNAUtils

dna = 'ATGATAGGCCTA'
du = DNAUtils(dna)

class GenoKenTest(unittest.TestCase):

    def test_read_dna_file(self):
        pass
    
    def test_transcribe(self):
        pass
    
    def test_blast_record(self):
        pass
    
    @GenokenUtils.timerlogging
    def test_complement(self):
        assert (du.complement()) == 'TACTATCCGGAT'
    
    @GenokenUtils.timerlogging
    def test_reverse_complement(self):
        assert (du.reverse_complement()) == 'TAGGCCTATCAT'

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    unittest.main(testRunner=runner)