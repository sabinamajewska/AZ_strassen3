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

# DOPISAĆ: funkcja dzieląca macierz na bloki

def adjust_size (matrix): #sprawdzam czy macierz jest rozmiaru 3^k
    size = len(matrix)
    power = 1
    while (size > power):
        power = power*3

    if size == power
        then
            matrix = matrix
        else
            difference = power - size
            matrix = #muszę tu dodać kolumny i wersze zer w ilości difference



#Przykład
A = load_matrix_B_from_file("matrix_example_1.txt")
B = load_matrix_A_from_file("matrix_example_2.txt")
print(A)
print(B)
print(is_square(A))
print(is_square(B))