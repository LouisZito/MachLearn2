#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 10:22:49 2020

@author: laz
"""
import matplotlib.pyplot as plt
import numpy as np

# =============================================================================
# note special coding as automaticaly sorts "stun"
# by alphabetical sequence, distoring Graph
# not needed with both x/y being numerical points
# =============================================================================

stun = ['delhi', 'surat', 'kolkata', 'mumbai', 'assam','bihar']
pop = np.array([1.9, 0.44, 0.45, 1.84, 3.00, 9.9])

#fig size is inches
figure = plt.figure(figsize=(8,3))

#due to alphabatizing names, use xtics
plt.xticks(range(len(pop)),stun)
#x,y
plt.plot(pop)
plt.title("States and Union Population Graph")
plt.ylabel("Population", color='r', fontsize=8, fontweight='bold')
plt.xlabel("States and Union Territory",color='b')
plt.show()
