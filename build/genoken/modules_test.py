# -*- coding: utf-8 -*-
#!usr/bin/env python3
#Created by Kenny William Nyallau 2020

import unittest
#import pytest
import os
from fasta.fastautil import FastaUtils
from misc.util import GenokenUtils
from dna.dnautil import DNAUtils

short_seq = 'ATGATAGGCCTA'
du = DNAUtils(short_seq)
DATA_DIR = os.path.join(os.path.abspath(os.curdir), 'data')

def test_read_singlefasta_file(file='simple.fasta'):
    ls_records_len, _, _, record_count, _ = test_read_multifasta_file(file)
    assert max(ls_records_len) == 990 and min(ls_records_len) == 990 and record_count == 1

def test_read_multifasta_file(file='dna2.fasta'):
    fu = FastaUtils(os.path.join(DATA_DIR, file))
    ls_records_len, _, _, record_count, _  = fu.get_fasta_record_info()
    return ls_records_len, _, _, record_count, _
    assert max(ls_records_len) == 4894 and min(115) and record_count == 18

def test_wrong_directory(file='simple.fasta'):
    try:
        fu = FastaUtils(os.path.join(DATA_DIR2, file))
    except NameError:
        raise

def test_wrong_file(file='simpler.fasta'):
    try:
        fu = FastaUtils(os.path.join(DATA_DIR, file))
        fu.get_fasta_record_info()
    except FileNotFoundError:
        raise

class GenoKenTest(unittest.TestCase):
    def test_read_dna_file_error(self):
        self.assertRaises(NameError, test_wrong_directory)
    
    def test_wrong_file_error(self):
        self.assertRaises(FileNotFoundError, test_wrong_file)
    
    @GenokenUtils.timerlogging
    def test_read_dna_file(self):
        test_read_singlefasta_file()
        test_read_multifasta_file()
    
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