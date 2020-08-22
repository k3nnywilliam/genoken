import unittest
from fasta.fastautil import FastaUtils
from miscutil.util import *

class GenoKenTest(unittest.TestCase):
    
    @timer_logging
    def test_read_dna_file(self):
        pass
    
    def test_transcribe(self):
        pass
    
    @timer_logging
    def test_blast_alignment(self):
        result = 25 * 3
        self.assertEqual(result, 50)

    def test_reverse_complement(self):
        pass

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    unittest.main(testRunner=runner)