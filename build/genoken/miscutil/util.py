# -*- coding: utf-8 -*-
#Created by Kenny William Nyallau 2020
import os

class Generate_Dictionary(dict):
    def __init__(self): 
        self = dict() 

    def add(self, key, value): 
        self[key] = value

class Utils:
  def timer_logging(func):
    def timer_wrapper(self,*args, **kwargs):
      import datetime                 
      start = datetime.datetime.now()                     
      result = func(self,*args, **kwargs)
      end = datetime.datetime.now()               
      print(f"\nElapsed Time Log = {end-start}")
      return result
    return timer_wrapper

  def get_data_directory(self, data):
    cur_path = os.getcwd()
    datapath = os.path.join(cur_path, data)
    return datapath
