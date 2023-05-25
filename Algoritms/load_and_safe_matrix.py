from Algoritms.functions import *


def load_matrix_from_file(filepath):
    loaded_matrix_A = []
    with open(filepath) as f:
        for line in f.readlines():
            line_ints = [int(s) for s in line.split(' ')]  # rzutujemy linię wejścia na listę intów
            loaded_matrix_A.append(line_ints)
    return matrix(loaded_matrix_A)  # matrix() z listy list robi reprezentację macierzową


def save_stand_mnoz_to_file(matrix_A, matrix_B, filepath):  # funkcja zapisująca macierz do pliku
    f = open(filepath, "w")
    f.write(str(stand_mnoz(matrix_A, matrix_B)))
    f.close()
    return


# PROTOTYP FUNKCJI SCZYTUJĄCEJ DWIE MACIERZE Z JEDNEGO PLIKU (jeszcze nie działa):

# def load_matrices_from_file(filepath):
#     loaded_matrix_A = []
#     loaded_matrix_B = []
#     with open(filepath) as f:
#         for line in f.readlines():
#             if line[0] != '!':
#                 line_ints = [int(s) for s in line.split(' ')]
#                 loaded_matrix_A.append(line_ints)
#             else:
#                 line_ints = [int(s) for s in line.split(' ')]
#                 loaded_matrix_B.append(line_ints)
#     A = matrix(loaded_matrix_A)
#     B = matrix(loaded_matrix_B)
#     return A, B
#
# print(load_matrices_from_file("matrices_to_load.txt"))

# save_stand_mnoz_to_file(load_matrix_from_file("matrices_to_load.txt"), "result_1")
# print(load_matrix_from_file("matrices_to_load.txt"))
