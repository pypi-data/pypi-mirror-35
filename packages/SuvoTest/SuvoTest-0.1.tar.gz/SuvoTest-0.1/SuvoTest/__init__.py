# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 13:54:21 2018

@author: suvod
"""

import math
import pandas as pd
import numpy as np

class action(object):
    
    def __init__(self,activation):
        self.activation = activation
    
    def actionMove(self,data):
        if self.activation == 'A':
            print("Move Left", data)
        else:
            print("Move Right", data)
            


