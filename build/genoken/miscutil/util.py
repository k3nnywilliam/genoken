# -*- coding: utf-8 -*-
#Created by Kenny William Nyallau 2020
import os

class Generate_Dictionary(dict):
    def __init__(self): 
        self = dict() 

    def add(self, key, value): 
        self[key] = value

class GenokenUtils:
  def timer_logging(func):
    def timer_wrapper(self,*args, **kwargs):
      import datetime                 
      start = datetime.datetime.now()                     
      result = func(self,*args, **kwargs)
      end = datetime.datetime.now()               
      print(f"\nElapsed Time Log = {end-start}")
      return result
    return timer_wrapper

  def get_fasta_data(self):
    '''
    Get a list of fasta files in data directory
    '''
    DATA_DIR = os.path.join(os.path.abspath(os.curdir), 'data')
    files = list()
    if os.path.exists(DATA_DIR):
        for f in os.listdir(DATA_DIR):
            files.append(f)
        s_files = sorted(files)
        return s_files
    else:
      print("{DATA_DIR} does not exist!")
