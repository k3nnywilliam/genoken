# -*- coding: utf-8 -*-
#Created by Kenny William Nyallau 2020
import os
import datetime

class Generate_Dictionary(dict):
    def __init__(self): 
        self = dict() 

    def add(self, key, value): 
        self[key] = value

class GenokenUtils:
  @staticmethod
  def timerlogging(func):
    def timer_wrapper(*args, **kwargs):          
      start = datetime.datetime.now()                     
      result = func(*args, **kwargs)
      end = datetime.datetime.now()               
      print(f"\nElapsed Time = {end-start}")
      return result
    return timer_wrapper
  
  @staticmethod
  def get_fasta_data(*args, **kwargs):
    DATA_DIR = os.path.join(os.path.abspath(os.curdir), 'data')
    files = list()
    if os.path.exists(DATA_DIR):
        for f in os.listdir(DATA_DIR):
            files.append(f)
        s_files = sorted(files)
        return s_files
    else:
      print("{DATA_DIR} does not exist!")
