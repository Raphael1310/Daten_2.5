# -*- coding: utf-8 -*-
import random
import sys
from timeit import default_timer as timer

def multiply_matrices(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        print("Cannot muliply matrices")
        sys.exit(0)
   
    matrix3 = [ [ 0 for i in range(len(matrix2[0]))] for h in range(len(matrix1))]
    for x in range(len(matrix3[0])):
       for y in range(len(matrix3)): 
         for z in range(len(matrix2)):
             matrix3[x][y] += matrix1[x][z]*matrix2[z][y]
             
    return matrix3
    
def create_matrix_random(row, column):
    matrix = [ [ 0 for i in range(column)] for h in range(row)]
    for x in range(row):
        for y in range(column):
            matrix[x][y]= random.randint(0,9)
            
    return matrix
            
# =============================================================================
# test für multiplikationsfunktion
# random.seed(42)   
# 
# m1 = create_matrix_random(3,4)
# m2 = create_matrix_random(4,3)
# m3 = multiply_matrices(m1,m2)
# 
# 
# print(m1)
# print(m2)
# print(m3)
# 
# 
# =============================================================================

start = timer()
list1 = []
list2 = []
list3 = []
for a in range(10):
    list1.append(create_matrix_random(200,200))
    end = timer()
    print("create matrix1", a, end-start)
    
    list2.append(create_matrix_random(200,200))
    end = timer()
    print("create matrix2", a, end-start)
    
    list3.append(multiply_matrices(list1[a],list2[a]))
    end = timer()
    print("multiply",a, end-start)