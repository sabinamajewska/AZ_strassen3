from Algoritms.functions import *
import time


def time_it(A, B):
    start_stand_multiplycation = time.time()
    stand_multiplycation(A, B)
    end_stand_multiplycation = time.time()
    start_multiply_matrices_strassen = time.time()
    multiply_matrices_strassen(A, B)
    end_multiply_matrices_strassen = time.time()
    return [end_stand_multiplycation - start_stand_multiplycation, end_multiply_matrices_strassen - start_multiply_matrices_strassen]
