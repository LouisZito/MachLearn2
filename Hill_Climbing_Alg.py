#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 10:55:43 2020
@author: Louis Zito 2095552
ML 2, PA 1-A, Hill Climbing Alg
"""
import numpy as np
import random
output = open("Hill_Climbing_Output.txt","w")
#boolean to trigger end condition
continue_cond = True
counter = 1

#user input for no. of bits
v = 0

#number of "1s" per chromosome
one = 0
#vc for current best fit, vn for next generated best fit comparison
vc = 0
vn = 0

def fitness_calc(matrix_fitness_added):
     matrix_of_sums = abs((13 * (np.sum(matrix_fitness_added, axis=0)) - 170))

     matrix_with_fitness = np.vstack((matrix_fitness_added,matrix_of_sums))
     return matrix_with_fitness

# def highest_vc(matrix):
#      start_chrome = 0
#      vc = matrix[12,start_chrome]
#      for column in matrix.T:
#           if vc > matrix[12,start_chrome]:
#                vc == matrix[12,start_chrome]
#           start_chrome = start_chrome + 1
#      print("\nFound Vc is " + str(vc))
#      return vc

     

#mutation of neighbor population of 30 each with a 1 bit muatation               
def generate_neighbors_for_muatation(matrix):
     #randomly chosen column
     #vc saved, mutated in one bit 30x
     #vc / vn comparison with largest returned each loop iteration
     #Isolate random chrome to generate mutated neighbor pop
       rand_chrome = random.randint(0,4)
       chrome_vc = matrix[:,rand_chrome]
       #reshape into column and copy 30xs
       chrome_vc = chrome_vc.reshape(-1,1)      
       thirty_clones_to_mute = np.tile(([chrome_vc]),(1,10))
       thirty_clones_to_mute = thirty_clones_to_mute[0,:,:]     
       print(thirty_clones_to_mute)
       return thirty_clones_to_mute
       
def original_vc(matrix):
     vc = matrix[12,0]
     return vc

def mutation_of_neighbor_clone(neighborhood):
     # # #remove fitness calculations for new mutated matrix fitness
     # print("Neigh Mat with deleted bottom row")
     # print(neighborhood)
     start_chrome = 0
     for column in neighborhood.T:
          locus = random.randint(0,11) 
          mutate_value = random.randint(0,1) 
          #mutated value added randomly to starting chromosome
          neighborhood[locus][start_chrome]=mutate_value
          start_chrome = start_chrome + 1
     neighborhood = np.delete(neighborhood, 12, axis = 0)
     #fitness_calc(neighborhood)
     return neighborhood


#sorting matrix in descending order of "1"s occurance
#sorted_matrix = matrix[:, np.argsort(-matrix.sum(axis=0))]       
def matrix_sort():
     sorted_matrix = matrix[:, np.argsort(-matrix.sum(axis=0))]
     return sorted_matrix

def vc_vn_comparison(neighbors, vc):
     current_chrome = 0
     for column in neighbors.T:
          vn = neighbors[12,current_chrome]
          print("Vc is: " + str(vc) + " and Vn is: " + str(vn))
          if vc < neighbors[12,current_chrome]:
               vc = neighbors[12,current_chrome]
          current_chrome = current_chrome + 1
     print(vc)
     output.write(str(vc) + ", ")
          

# populate initial random matrix of chromosomes
col = 5
row = 12
output.write("\nLouis Zito, PA1-A, Hill Climbing Output:\n")
print("Starting population")
matrix = np.random.randint(2,size=(row, col))
print(matrix)

#while continue_cond:
     # matrix = matrix_sort()
     # print("\n")
     # print("sorted matrix")
     # print(matrix)
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
     # print("\n")
     # print("mutated matrix")
     # print(neighbor_matrix)
     # matrix = matrix_sort()
     # print("\n")
     # print("sorted matrix")
     # print(matrix)
     #matrix = fitness_calc()
print("\n")    
     # counter +=counter
     # if counter > 1:
     #      continue_cond = False

output.close()    
    
    
    
    
    
    
    
    