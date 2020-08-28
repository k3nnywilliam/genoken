import unittest
from fasta import fastautil as fst
from miscutil.util import GenokenUtils

class GenoKenTest(unittest.TestCase):
    
    @GenokenUtils.timerlogging
    def test_read_dna_file(self):
        pass
    
    def test_transcribe(self):
        pass
    
    @GenokenUtils.timerlogging
    def test_blast_record(self):
        pass

    def test_multifasta(self):
        pass

    def test_reverse_complement(self):
        pass

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    unittest.main(testRunner=runner)