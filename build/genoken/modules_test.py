import unittest
import pytest
import os
from fasta.fastautil import FastaUtils
from miscutil.util import GenokenUtils
from dnautil.dnautil import DNAUtils

dna = 'ATGATAGGCCTA'
du = DNAUtils(dna)
DATA_DIR = os.path.join(os.path.abspath(os.curdir), 'data')
fu = FastaUtils(os.path.join(DATA_DIR, 'simple.fasta'))

def test_read_singlefasta_file(file='simple.fasta'):
    test_read_multifasta_file(file)

def test_read_multifasta_file(file='dna2.fasta'):
    fu = FastaUtils(os.path.join(DATA_DIR, file))
    ls_records_len, _, _, record_count, _  = fu.get_fasta_record_info()
    assert max(ls_records_len) > 990 and record_count > 1

class GenoKenTest(unittest.TestCase):
    def test_read_dna_file_error(self):
        if not DATA_DIR:
            raise self.assertRaises(Exception("File not found"))
        else:
            return "File ok"
    
    @GenokenUtils.timerlogging
    def test_read_dna_file(self):
        test_read_singlefasta_file()
        #ls_records_len, _, _, record_count, _  = fu.get_fasta_record_info()
        #assert max(ls_records_len) == 990 and record_count == 1
    
    @GenokenUtils.timerlogging
    def test_transcribe(self):
        assert du.transcribe() == 'AUGAUAGGCCUA'
    
    @GenokenUtils.timerlogging
    def test_complement(self):
        assert du.complement() == 'TACTATCCGGAT'
    
    @GenokenUtils.timerlogging
    def test_reverse_complement(self):
        assert du.reverse_complement() == 'TAGGCCTATCAT'

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    unittest.main(testRunner=runner)