# -*- coding: utf-8 -*-
#Created by Kenny William Nyallau 2020

class Logging: 
    def __init__(self, func):
        self.func = func
  
    def __call__(self, *args, **kwargs):
      print(f'Before {self.func.__name__}')
      self.function(self, *args, **kwargs)
      print(f'After {self.func.__name__}')


def timer_logging(func):
  def timer_wrapper(*args, **kwargs):
    import datetime                 
    start = datetime.datetime.now()                     
    result = func(*args, **kwargs)
    end = datetime.datetime.now()               
    print(f"\nElapsed Time Log = {end-start}")
    return result
  return timer_wrapper