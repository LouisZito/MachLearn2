#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 10:55:43 2020
@author: Louis Zito 2095552
ML 2, PA 1-B, Simulated Annealing Alg
"""
#numpy used for all matrix manipulation, math for e^x, random for chrome selection/mutates
import numpy as np
import math
import random
#included output text file
output = open("L_Zito_Sim_Annealing_Output.txt","w")
#temperature variable and comparison rand value 0-1 for temp check
temp = 100
rand_temp_comparison = 0
#boolean to trigger end condition with while-counter
continue_cond = True
counter = 1
#number of "1s" per chromosome
one = 0
#vc for current best fit, vn for next-generated best fit comparison
vc = 0
vn = 0

#Self-Anneal Temp varaible/func included to allow accepting lower Vn vals
def temp_function(vc, vn, temp):
     #calculation of exponent for e^x
     e_expo = (vn -vc)/temp
     #e^x final output to be used if Vn<Vc and e^x value > rand(0-1)
     e_val = round(math.exp(e_expo),4)
     print("Calculated e^x: " + str(e_val))
     return e_val

#fitness formula from directions applied to primary matrix and neighbor matrix
def fitness_calc(matrix_fitness_added):
     matrix_of_sums = abs((14 * (np.sum(matrix_fitness_added, axis=0)) - 190))
     #fusion of original matrix with row containing indexed fitness values
     matrix_with_fitness = np.vstack((matrix_fitness_added,matrix_of_sums))
     print(matrix_with_fitness)
     return matrix_with_fitness

#generate neighbor population of 40 chrome for mutation              
def generate_neighbors_for_muatation(matrix):
     #randomly chosen column
     #generates 40 copies to be mutated in "mutation" func below
       #rand chrome selection from starting pop
       rand_chrome = random.randint(0,50)
       chrome_vc = matrix[:,rand_chrome]
       #reshape into column and copy 30xs
       chrome_vc = chrome_vc.reshape(-1,1)      
       clones_to_mute = np.tile(([chrome_vc]),(1,50))
       #cut unneeded tiled = 3rd dimension off neighbor population from prev line
       clones_to_mute = clones_to_mute[0,:,:]     
       print(clones_to_mute)
       return clones_to_mute

#function returns starting pop Vc from row 12 of orginal matrix each iteration
def original_vc(matrix):
     vc = matrix[50,0]
     return vc

#mutation func, altering 1 bit in the neighborhood pop of 40 chromosomes
def mutation_of_neighbor_clone(neighborhood):
     start_chrome = 0
     for column in neighborhood.T:
          #bit location to mutate
          locus = random.randint(0,49) 
          #bit value location will mututate to
          mutate_value = random.randint(0,1) 
          #mutated value added randomly to starting chromosome
          neighborhood[locus][start_chrome]=mutate_value
          start_chrome = start_chrome + 1
     #deletes row 12 containing old fitness row for updated fitness calc
     neighborhood = np.delete(neighborhood, 50, axis = 0)
     return neighborhood


#sorting matrix in descending order of "1"s occurance     
def matrix_sort():
     sorted_matrix = matrix[:, np.argsort(-matrix.sum(axis=0))]
     return sorted_matrix

#for loop comparison of best Vc to current chrome Vn in neighbors
#if Vn higher, overwrite Vc else loop to next chromosome
def vc_vn_comparison(neighbors, vc, temp):
     rand_temp_comparison = random.randint(0,1)
     print("\nRandom Comparitor 0-1 for Temp: " + str(rand_temp_comparison))
     #single rand chrome from muated neighbors chosen
     rand_mutated_chrome = random.randint(0,49)
     #initialize vn for fitness of that single chrome
     vn = neighbors[50,rand_mutated_chrome]
     #calc e_val for use if vc larger + elif conditions
     e_val = temp_function(vc, vn, temp)
     #vc < vn = overwrite
     if vc < neighbors[50,rand_mutated_chrome]:
          vc = neighbors[50,rand_mutated_chrome]
     #else: if rand_temp_comp 0-1 is less than the e_val returns above,
     elif rand_temp_comparison < e_val:
          #overwrite vc, regardless of vn being lower
          #a higher temp/earlier in While loop with inc. % of this occuring
          vc = neighbors[50,rand_mutated_chrome]
     print("\nVc: " + str(vc) + ", Vn: " + str(vn))
     print("Final Vc result: " + str(vc))
     output.write(str(vc) + ", ")
 
#main program loop running 100 times
#generates one highest Vc for each iteration         
while continue_cond:
     print("While-Counter: " + str(counter))
     if temp <=0:
          continue_cond = False
     if counter >= 200:
          continue_cond = False
     # populate initial random matrix of chromosomes
     col = 250
     row = 50
     print("\nStarting population")
     matrix = np.random.randint(2,size=(row, col))
     print(matrix)

     print("\nstarting pop with fitness appended")
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

     print("\ntemp is: " + str(temp))
     print("\nVc vs single-random Vn comparison: ")
     vc_vn_comparison(fit_mutated_neighbors, vc, temp)
     print("\n")    
     counter = counter + 1
     temp = round(temp - 0.5,1)
     
output.write("\n\n@author: Louis Zito 2095552 Simulated Annealing Alg")
output.close()    
    
    
    
    
    
    
    
    