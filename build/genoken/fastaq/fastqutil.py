import os

def readFastq(filename):
    sequences = list()
    qualities = list()
    with open(filename) as fh:
        while True:
            fh.readline()
            seq = fh.readline().rstrip()
            fh.readline()
            qual = fh.readline().rstrip()
            if len(seq) == 0:
                break
            sequences.append(seq)
            qualities.append(qual)
    return sequences, qualities

DATA_DIR = os.path.join(os.path.abspath(os.curdir), 'data')

seq, qual = readFastq(os.path.join(DATA_DIR, 'SRR835775_1.first1000.fastq'))

