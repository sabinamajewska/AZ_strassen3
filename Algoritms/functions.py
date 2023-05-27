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
    # matrix = adjust_size(matrix)  # chcemy dzielić macierze postaci 3^k
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


#mat = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]]
# mat = matrix(mat)
# sizeM = len(mat)
# M1 = mat[0:int(sizeM / 3), 0:int(sizeM / 3)]
# M2 = mat[0:int(sizeM / 3), int(sizeM / 3):int(2 * sizeM / 3)]
# M3 = mat[0:int(sizeM / 3), int(2 * sizeM / 3):int(sizeM)]
#
# print(mat)
# print(M1)
# print(M2)
# print(M1 + M2)

def strassen(A, B):
    m = len(A)
    if m == 1:
        return A * B
    else:
        splitA = split(A)
        splitB = split(B)
        M1 = strassen(splitA[0] + splitA[1] + splitA[2] - splitA[3] - splitA[4] - splitA[7] - splitA[8],
                      splitB[4])
        M2 = strassen(splitA[0] - splitA[3], -splitB[1] + splitB[4])
        M3 = strassen(splitA[4],
                      -splitB[0] + splitB[1] + splitB[3] - splitB[4] - splitB[5] - splitB[6] + splitB[8])
        M4 = strassen(-splitA[0] + splitA[3] + splitA[4], splitB[0] - splitB[1] + splitB[4])
        M5 = strassen(splitA[3] + splitA[4], -splitB[0] + splitB[1])
        M6 = strassen(splitA[0], splitB[0])
        M7 = strassen(-splitA[0] + splitA[6] + splitA[7], splitB[0] - splitB[2] + splitB[5])
        M8 = strassen(-splitA[0] + splitA[6], splitB[2] - splitB[5])
        M9 = strassen(splitA[6] + splitA[7], -splitB[0] + splitB[2])
        M10 = strassen(splitA[0] + splitA[1] + splitA[2] - splitA[4] - splitA[5] - splitA[6] - splitA[7],
                       splitB[5])
        M11 = strassen(splitA[7],
                       -splitB[0] + splitB[2] + splitB[3] - splitB[4] - splitB[5] - splitB[6] + splitB[7])
        M12 = strassen(-splitA[2] + splitA[7] + splitA[8], splitB[4] + splitB[6] - splitB[7])
        M13 = strassen(splitA[2] - splitA[8], splitB[4] - splitB[7])
        M14 = strassen(splitA[2], splitB[6])
        M15 = strassen(splitA[7] + splitA[8], -splitB[6] + splitB[7])
        M16 = strassen(-splitA[2] + splitA[4] + splitA[5], splitB[5] + splitB[6] - splitB[8])
        M17 = strassen(splitA[2] - splitA[5], splitB[5] - splitB[8])
        M18 = strassen(splitA[4] + splitA[5], -splitB[6] + splitB[8])
        M19 = strassen(splitA[1], splitB[3])
        M20 = strassen(splitA[5], splitB[7])
        M21 = strassen(splitA[3], splitB[2])
        M22 = strassen(splitA[6], splitB[1])
        M23 = strassen(splitA[8], splitB[8])

        C11 = M6 + M14 + M19
        C12 = M1 + M4 + M5 + M6 + M12 + M14 + M15
        C13 = M6 + M7 + M9 + M10 + M14 + M16 + M18
        C21 = M2 + M3 + M4 + M6 + M14 + M16 + M17
        C22 = M2 + M4 + M5 + M6 + M20
        C23 = M14 + M16 + M17 + M18 + M21
        C31 = M6 + M7 + M8 + M11 + M12 + M13 + M14
        C32 = M12 + M13 + M14 + M15 + M22
        C33 = M6 + M7 + M8 + M9 + M23

        C_1 = np.concatenate((C11, matrix(np.concatenate((C21, C31)))))
        C_2 = np.concatenate((C12, matrix(np.concatenate((C22, C32)))))
        C_3 = np.concatenate((C13, matrix(np.concatenate((C23, C33)))))
        C = np.concatenate((C_1, matrix(np.concatenate((C_2, C_3), axis=1))), axis=1)

        return C


# mat1 = [[1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1]]
# mat2 = [[2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2, 2]]
# res = strassen(matrix(mat1), matrix(mat2))
# print(res)

# pierwotna wersja
# def multiply_matrices_strassen(A, B):
#     m = len(A)
#     if adjust_size(A).all() == A.all():
#         helper = 1
#         AA = A
#         BB = B
#     else:
#         helper = 0
#         AA = adjust_size(A)
#         BB = adjust_size(B)
#     result = strassen(AA, BB)
#     if helper == 1:
#         return result
#     else:
#         return result[0:m, 0:m]


def multiply_matrices_strassen(A, B):
    m = len(A)
    AA = adjust_size(A)
    BB = adjust_size(B)
    result = strassen(AA, BB)
    if m == len(AA):
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

