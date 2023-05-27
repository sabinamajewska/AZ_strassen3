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

# PRZYKLAD
save_multiply_matrices_to_file(load_matrix_from_file("../Example/generated_matrix_1.txt"),
                               load_matrix_from_file("../Example/generated_matrix_2.txt"), "../Example/wyniczek.txt")
