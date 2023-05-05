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

def save_matrix_to_file(matrix_example, filepath): # funkcja zapisująca macierz do pliku
    f = open(filepath, "w")  # "w" oznacza, że jeżeli plik nie isnieje, to zostanie utworozny, jeżeli istnieje, to go nadpiszemy
    f.write(str(adjust_size(matrix_example))) #tutaj akurat zapisuję macierz powstałą w funkcji pomocniczej
    f.close()
    return

#Przykład
A = load_matrix_B_from_file("matrix_example_1.txt")
B = load_matrix_A_from_file("matrix_example_2.txt")
print(A)
print(adjust_size(A))
print(B)
print(adjust_size(B))
print(is_square(A))
print(is_square(B))
save_matrix_to_file(A,"adjust_size_example_1")