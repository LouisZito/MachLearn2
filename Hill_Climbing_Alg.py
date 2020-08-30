#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 10:55:43 2020
@author: Louis Zito 2095552
ML 2, PA 1, Hill Climbing Alg
"""
import numpy as np
import random
#boolean to trigger end condition
end_cond = False

#user input for no. of bits
v = 0

#number of "1s" per chromosome
one = 0

# populate initial random matrix of chromosomes
col = 10
row = 11
print("Starting population")
matrix = np.random.randint(2,size=(row, (col-1)))
print(matrix)
    
def fitness_calc():
    #res = [sum(x) for x in zip(*matrix)]
    #print("\n")
    #print(res)
    #print("\n")
    #print(res[0])
    print("\n")
    
def sort_matrix():
     print("\n")
     print("Sorted population by fitness")
     sorted_matrix = matrix[:, np.argsort(matrix.sum(axis=0))]
     print(sorted_matrix)
     print("\n")

                   
def mutate():
     print("Mutated Population")
     start_chrome = 0
     for row in range(0, 9):
       loci = random.randint(0,10)
       mutate_value = random.randint(0,1) 
       print("loci: " + str(loci) + " Mute Value " + str(mutate_value))
       matrix[loci][start_chrome]=mutate_value
       start_chrome = start_chrome + 1
      
sort_matrix()
fitness_calc()
mutate()

print("\n")
for row in matrix:
    print(row)