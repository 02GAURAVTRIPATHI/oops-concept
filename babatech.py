# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 17:38:09 2020

@author: gaurav baba
"""

class Laptop:
    
  def __init__(self, model, price): # constructor
        
        self.model = model
        self.price = price
  
  def showmodel(self):
     print("Model:", self.model, "price:", self.price)

ashu = Laptop('ASHU', 20000)
ashu.showmodel()
print(id(ashu))
print()
            
lenovo = Laptop('LENOVO', 32000)
lenovo.showmodel()
print(id(lenovo))
print()
            
hp = Laptop('HP', 30000)
hp.showmodel()
print(id(hp))