from numpy import matrix
def load_matrix_A_from_file(filepath):
    loaded_matrix_A = []  # to będzie nasza macierz A
    with open(filepath) as f:
        for line in f.readlines():
            line_ints = [int(s) for s in line.split(' ')]  # rzutujemy linię wejścia na listę intów
            loaded_matrix_A.append(line_ints)
    return matrix(loaded_matrix_A) # funkcja matrix z listy list robi reprezentację macierzową
def load_matrix_B_from_file(filepath):
    loaded_matrix_B = []  # to będzie nasza macierz B
    with open(filepath) as f:
        for line in f.readlines():
            line_ints = [int(s) for s in line.split(' ')]  # rzutujemy linię wejścia na listę intów
            loaded_matrix_B.append(line_ints)

    return matrix(loaded_matrix_B) # funkcja matrix z listy list robi reprezentację macierzową

def is_square (matrix):
    return len(matrix) == len(matrix.T) # sprawdzam czy liczba wierszy w macierzy A i w macierzy A transponowanej jest równa

def adjust_size (matrix_example): #sprawdzam czy dana macierz kwadratowa jest rozmiaru 3^k
    size = len(matrix_example)
    power = 1
    while (size > power):
        power = power*3

    if size == power:
        result = matrix_example
    else:
        result = matrix([[0 for x in range(power)] for y in range(power)])
        result[0:len(matrix_example), 0:len(matrix_example)] = matrix_example
    return result

def split(matrix_example):
    matrix_example = adjust_size(matrix_example) #chcemy dzielić macierze postaci 3^k
    size = len(matrix_example)

    A11 = matrix_example[0:int(size / 3), 0:int(size / 3)]
    A12 = matrix_example[0:int(size / 3), int(size / 3):int(2 * size / 3)]
    A13 = matrix_example[0:int(size / 3), int(2 * size / 3):int(size)]
    A21 = matrix_example[int(size / 3):int(2 * size / 3), 0:int(size / 3)]
    A22 = matrix_example[int(size / 3):int(2 * size / 3), int(size / 3):int(2 * size / 3)]
    A23 = matrix_example[int(size / 3):int(2 * size / 3), int(2 * size / 3):int(size)]
    A31 = matrix_example[int(2 * size / 3):int(size), 0:int(size / 3)]
    A32 = matrix_example[int(2 * size / 3):int(size), int(size / 3):int(2 * size / 3)]
    A33 = matrix_example[int(2 * size / 3):int(size), int(2 * size / 3):int(size)]
    return A11, A12, A13, A21, A22, A23, A31, A32, A33


def stand_mnoz(A, B):
    if len(A.T) != len(B):
        print("Macierze są złych wymiarów.")
    else:
        result = matrix([[0 for x in range(len(B.T))] for y in range(len(A))])
        for i in range(len(A)):
            for j in range(len(B.T)):
                result[i, j] = sum(A[i]*(B.T[j]).T)
        return result

def save_stand_mnoz_to_file(matrix_A, matrix_B, filepath): # funkcja zapisująca macierz do pliku
    f = open(filepath, "w")  # "w" oznacza, że jeżeli plik nie isnieje, to zostanie utworozny, jeżeli istnieje, to go nadpiszemy
    f.write(str(stand_mnoz(matrix_A, matrix_B))) #tutaj akurat zapisuję macierz powstałą w funkcji pomocniczej
    f.close()
    return

#Przykład
A = load_matrix_B_from_file("matrix_example_1.txt")
B = load_matrix_A_from_file("matrix_example_2.txt")
# print(A)
# print(adjust_size(A))
# print(B)
# print(adjust_size(B))
# print(is_square(A))
# print(is_square(B))
# save_stand_mnoz_to_file(A, B,"stand_mnoz_example_1")
print(split(adjust_size(B)))

C=matrix([[1,0,0],[0,1,0],[0,0,1]])
D=matrix([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
# print(stand_mnoz(C,D))
