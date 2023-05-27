from Algoritms.functions import *
import time


def time_it(A, B):
    start_stand_mnoz = time.time()
    stand_result = stand_multiplycation(A, B)
    end_stand_mnoz = time.time()
    start_multiply_matrices_strassen = time.time()
    strassen_result = multiply_matrices_strassen(A, B)
    end_multiply_matrices_strassen = time.time()
    if stand_result.all() != strassen_result.all():
        print("Different results")
    return [end_stand_mnoz - start_stand_mnoz, end_multiply_matrices_strassen - start_multiply_matrices_strassen]
