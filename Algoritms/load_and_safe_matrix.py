from Algoritms.functions import *
from Algoritms.timer import time_it


def load_matrix_from_file(filepath):
    loaded_matrix_A = []
    with open(filepath) as f:
        for line in f.readlines():
            line_ints = [int(s) for s in line.split(' ')]  # rzutujemy linię wejścia na listę intów
            loaded_matrix_A.append(line_ints)
    return matrix(loaded_matrix_A)  # matrix() z listy list robi reprezentację macierzową


def save_stand_multiplication_to_file(matrix_A, matrix_B, filepath):  # funkcja zapisująca macierz do pliku
    f = open(filepath, "w")
    f.write(str(stand_multiplycation(matrix_A, matrix_B)))
    f.close()
    return


def save_multiply_matrices_to_file(matrix_A, matrix_B, filepath):
    f = open(filepath, "w")
    f.write(str(multiply_matrices_strassen(matrix_A, matrix_B)) + '\n')
    time_result = time_it(matrix_A, matrix_B)
    f.write("Czas pracy algorytmu multiply_matrices_strassen dla podanych macierzy wejsciowych to "
            + str(time_result[1]) + '\n')
    f.write("Czas pracy algorytmu stand_multiplycation macierzy dla podanych macierzy wejsciowych to "
            + str(time_result[0]) + '\n')
    f.close()
    return


# # PRZYKLAD
#save_multiply_matrices_to_file(load_matrix_from_file("../Example/generated_matrix_1.txt"),
#                               load_matrix_from_file("../Example/generated_matrix_2.txt"), "../Example/example_out.txt")
