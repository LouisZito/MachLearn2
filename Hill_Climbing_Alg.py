#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 10:55:43 2020
@author: Louis Zito 2095552
ML 2, PA 1-A, Hill Climbing Alg
"""
#numpy used for all matrix manipulation
import numpy as np
#random used for chrom selections and mutations
import random
#included output text file
output = open("L_Zito_Hill_Climbing_Output.txt","w")
#boolean to trigger end condition with while-counter
continue_cond = True
counter = 1
#user input for no. of bits
v = 0
#number of "1s" per chromosome
one = 0
#vc for current best fit, vn for next-generated best fit comparison
vc = 0
vn = 0

#fitness formula from directions applied to primary matrix and neighbor matrix
def fitness_calc(matrix_fitness_added):
     matrix_of_sums = abs((13 * (np.sum(matrix_fitness_added, axis=0)) - 170))
     #fusion of original matrix with row containing indexed fitness values
     matrix_with_fitness = np.vstack((matrix_fitness_added,matrix_of_sums))
     return matrix_with_fitness

#generate neighbor population of 40 chrome for mutation              
def generate_neighbors_for_muatation(matrix):
     #randomly chosen column
     #generates 40 copies to be mutated in "mutation" func below
     #skip chrome 0, this chrome is used for starting rand Vc every run
       rand_chrome = random.randint(1,40)
       chrome_vc = matrix[:,rand_chrome]
       #reshape into column and copy 30xs
       chrome_vc = chrome_vc.reshape(-1,1)      
       clones_to_mute = np.tile(([chrome_vc]),(1,40))
       clones_to_mute = clones_to_mute[0,:,:]     
       print(clones_to_mute)
       return clones_to_mute

#function returns starting pop Vc from row 12 of orginal matrix each iteration
def original_vc(matrix):
     vc = matrix[40,0]
     return vc

#mutation func, altering 1 bit in the neighborhood pop of 40 chromosomes
def mutation_of_neighbor_clone(neighborhood):
     start_chrome = 0
     for column in neighborhood.T:
          #bit location to mutate
          locus = random.randint(0,40) 
          #bit value location will mututate to
          mutate_value = random.randint(0,1) 
          #mutated value added randomly to starting chromosome
          neighborhood[locus][start_chrome]=mutate_value
          start_chrome = start_chrome + 1
     #deletes row 12 containing old fitness row for updated fitness calc
     neighborhood = np.delete(neighborhood, 40, axis = 0)
     return neighborhood


#sorting matrix in descending order of "1"s occurance     
def matrix_sort():
     sorted_matrix = matrix[:, np.argsort(-matrix.sum(axis=0))]
     return sorted_matrix

#for loop comparison of best Vc to current chrome Vn in neighbors
#if Vn higher, overwrite Vc else loop to next chromosome
def vc_vn_comparison(neighbors, vc):
     current_chrome = 0
     for column in neighbors.T:
          vn = neighbors[40,current_chrome]
          print("Vc is: " + str(vc) + " and Vn is: " + str(vn))
          if vc < neighbors[40,current_chrome]:
               vc = neighbors[40,current_chrome]
          current_chrome = current_chrome + 1
     print("\nFinal Vc found: " + str(vc))
     output.write(str(vc) + ", ")
 
#main program loop running 100 times
#generates one highest Vc for each iteration         
while continue_cond:
     print(counter)
     if counter >= 100:
          continue_cond = False
     # populate initial random matrix of chromosomes
     col = 200
     row = 40
     print("Starting population")
     matrix = np.random.randint(2,size=(row, col))
     print(matrix)

     print("\nstarting pop with fitness added row 11")
     matrix = fitness_calc(matrix)

     print("\nMatrix of 30 Rnd chrome copies to mutate") 
     neighbors = generate_neighbors_for_muatation(matrix)

     print("\nvc saved from original")
     vc = original_vc(neighbors)
     print(vc)

     print("\nmutated neighbors")
     mutated_neighbors = mutation_of_neighbor_clone(neighbors)
     print(mutated_neighbors)

     print("\nmutated with fitness added")
     fit_mutated_neighbors = fitness_calc(mutated_neighbors)
     print(fit_mutated_neighbors)

     print("\nVc vs Vn in neighbors comparison: ")
     vc_vn_comparison(fit_mutated_neighbors, vc)
     print("\n")    
     counter = counter + 1
     
output.write("\n\n@author: Louis Zito 2095552 Hill Climbing Alg")
output.close()    
    
    
    
    
    
    
    
    