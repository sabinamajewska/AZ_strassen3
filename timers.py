from functions import *
import time

def time_it(A, B):
    start = time.time()
    stand_mnoz(A, B)
    end = time.time()
    return end - start

# PRZYKŁAD
A = load_matrix_A_from_file("matrix_example_1.txt")
B = load_matrix_A_from_file("matrix_example_2.txt")

print(time_it(A, B))