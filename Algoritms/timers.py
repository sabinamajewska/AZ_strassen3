# from Algoritms.load_and_safe_matrix import load_matrix_from_file
from functions import *
import time


def time_it(A, B):
    start_stand_mnoz = time.time()
    stand_mnoz(A, B)
    end_stand_mnoz = time.time()
    start_multiply_matrices_strassen = time.time()
    multiply_matrices_strassen(A, B)
    end_multiply_matrices_strassen = time.time()
    return [end_stand_mnoz - start_stand_mnoz, end_multiply_matrices_strassen - start_multiply_matrices_strassen]



# PRZYKŁAD
# A = load_matrix_from_file("../Example/matrix_example_1.txt")
# B = load_matrix_from_file("../Example/matrix_example_2.txt")
#
# print(time_it(A, B))
