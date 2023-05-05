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

def isSquare (matrix):
    return len(matrix) == len(matrix.T) # sprawdzam czy liczba wierszy w macierzy A i w macierzy A transponowanej jest równa

# funkcja dzieląca macierz na bloki

# funkcja sprawdzająca czy macieerz jest postaci 3^k i ewentualnie dopisująca kolumny i wiersze zer

#Przykład
A = load_matrix_B_from_file("matrix_example_1.txt")
B = load_matrix_A_from_file("matrix_example_2.txt")
print(A)
print(B)
print(isSquare(A))
print(isSquare(B))