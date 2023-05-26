import numpy as np
from numpy import matrix


def is_square(matrix):
    return len(matrix) == len(
        matrix.T)  # sprawdzam czy liczba wierszy w macierzy A i w macierzy A transponowanej jest równa


def adjust_size(matrix_example):  # sprawdzam czy dana macierz kwadratowa jest rozmiaru 3^k
    size = len(matrix_example)
    power = 1
    while size > power:
        power = power * 3

    if size == power:
        result = matrix_example
    else:
        result = matrix([[0 for x in range(power)] for y in range(power)])
        result[0:len(matrix_example), 0:len(matrix_example)] = matrix_example
    return result


def split(matrix):
    matrix = adjust_size(matrix)  # chcemy dzielić macierze postaci 3^k
    size = len(matrix)

    A11 = matrix[0:int(size / 3), 0:int(size / 3)]
    A12 = matrix[0:int(size / 3), int(size / 3):int(2 * size / 3)]
    A13 = matrix[0:int(size / 3), int(2 * size / 3):int(size)]
    A21 = matrix[int(size / 3):int(2 * size / 3), 0:int(size / 3)]
    A22 = matrix[int(size / 3):int(2 * size / 3), int(size / 3):int(2 * size / 3)]
    A23 = matrix[int(size / 3):int(2 * size / 3), int(2 * size / 3):int(size)]
    A31 = matrix[int(2 * size / 3):int(size), 0:int(size / 3)]
    A32 = matrix[int(2 * size / 3):int(size), int(size / 3):int(2 * size / 3)]
    A33 = matrix[int(2 * size / 3):int(size), int(2 * size / 3):int(size)]
    return A11, A12, A13, A21, A22, A23, A31, A32, A33


def strassen(A, B):
    m = len(A)
    if m == 1:
        return A * B
    else:
        M1 = strassen(split(A)[0] + split(A)[1] + split(A)[2] - split(A)[3] - split(A)[4] - split(A)[7] - split(A)[8],
                      split(B)[4])
        M2 = strassen(split(A)[0] - split(A)[3], -split(B)[1] + split(B)[4])
        M3 = strassen(split(A)[4],
                      -split(B)[0] + split(B)[1] + split(B)[3] - split(B)[4] - split(B)[5] - split(B)[6] + split(B)[8])
        M4 = strassen(-split(A)[0] + split(A)[3] + split(A)[4], split(B)[0] - split(B)[1] + split(B)[4])
        M5 = strassen(split(A)[3] + split(A)[4], -split(B)[0] + split(B)[1])
        M6 = strassen(split(A)[0], split(B)[0])
        M7 = strassen(-split(A)[0] + split(A)[6] + split(A)[7], split(B)[0] - split(B)[2] + split(B)[5])
        M8 = strassen(-split(A)[0] + split(A)[6], split(B)[2] - split(B)[5])
        M9 = strassen(split(A)[6] + split(A)[7], -split(B)[0] + split(B)[2])
        M10 = strassen(split(A)[0] + split(A)[1] + split(A)[2] - split(A)[4] - split(A)[5] - split(A)[6] - split(A)[7],
                       split(B)[5])
        M11 = strassen(split(A)[7],
                       -split(B)[0] + split(B)[2] + split(B)[3] - split(B)[4] - split(B)[5] - split(B)[6] + split(B)[7])
        M12 = strassen(-split(A)[2] + split(A)[7] + split(A)[8], split(B)[4] + split(B)[6] - split(B)[7])
        M13 = strassen(split(A)[2] - split(A)[8], split(B)[4] - split(B)[7])
        M14 = strassen(split(A)[2], split(B)[6])
        M15 = strassen(split(A)[7] + split(A)[8], -split(B)[6] + split(B)[7])
        M16 = strassen(-split(A)[2] + split(A)[4] + split(A)[5], split(B)[5] + split(B)[6] - split(B)[8])
        M17 = strassen(split(A)[2] - split(A)[5], split(B)[5] - split(B)[8])
        M18 = strassen(split(A)[4] + split(A)[5], -split(B)[6] + split(B)[8])
        M19 = strassen(split(A)[1], split(B)[3])
        M20 = strassen(split(A)[5], split(B)[7])
        M21 = strassen(split(A)[3], split(B)[2])
        M22 = strassen(split(A)[6], split(B)[1])
        M23 = strassen(split(A)[8], split(B)[8])

        C11 = M6 + M14 + M19
        C12 = M1 + M4 + M5 + M6 + M12 + M14 + M15
        C13 = M6 + M7 + M9 + M10 + M14 + M16 + M18
        C21 = M2 + M3 + M4 + M6 + M14 + M16 + M17
        C22 = M2 + M4 + M5 + M6 + M20
        C23 = M14 + M16 + M17 + M18 + M21
        C31 = M6 + M7 + M8 + M11 + M12 + M13 + M14
        C32 = M12 + M13 + M14 + M15 + M22
        C33 = M6 + M7 + M8 + M9 + M23

        C_1 = np.concatenate(C11, matrix(np.concatenate(C21, C31)))
        C_2 = np.concatenate(C12, matrix(np.concatenate(C22, C32)))
        C_3 = np.concatenate(C13, matrix(np.concatenate(C23, C33)))
        C = np.concatenate(C_1, matrix(np.concatenate(C_2, C_3, axis=1)), axis=1)

        return C


def multiply_matrices_strassen(A,B):
    m = len(A)
    if adjust_size(A)==A:
        helper = 1
        AA = A
        BB = B
    else:
        helper = 0
        AA = adjust_size(A)
        BB = adjust_size(B)
    result = strassen(AA, BB)
    if helper == 1:
        return result
    else:
        return result[0:m, 0:m]


def stand_mnoz(A, B):
    if len(A.T) != len(B):
        print("Macierze są złych wymiarów.")
    else:
        result = matrix([[0 for x in range(len(B.T))] for y in range(len(A))])
        for i in range(len(A)):
            for j in range(len(B.T)):
                result[i, j] = sum(A[i] * (B.T[j]).T)
        return result

# Przykłady
# A = load_matrix_B_from_file("matrix_example_1.txt")
# B = load_matrix_A_from_file("matrix_example_2.txt")
# print(A)
# print(adjust_size(A))
# print(B)
# print(adjust_size(B))
# print(is_square(A))
# print(is_square(B))
# save_stand_mnoz_to_file(A, B,"stand_mnoz_example_1")
# print(split(adjust_size(B)))
# C=matrix([[1,0,0],[0,1,0],[0,0,1]])
# D=matrix([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
# print(stand_mnoz(C,D))
