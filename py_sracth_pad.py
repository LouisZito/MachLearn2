#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 13:38:04 2020

@author: laz
"""
import numpy as np
import random
import math
#intialize starting temperature variable and comparison for temp check
temp = 100
rand_temp_comparison = 0

def temp_function(vc, vn, temp):
     rand_temp_comparison = random.randint(0,1)
     print(rand_temp_comparison)
     e_expo = (vn -vc)/temp
     print(e_expo)
     e_val = math.exp(e_expo)
     print(e_val)
     
temp_function(18,7,20) 

