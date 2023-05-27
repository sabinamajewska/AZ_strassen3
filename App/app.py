from Algoritms.load_and_safe_matrix import *


def app():
    A = load_matrix_from_file("../App/matrix_A.txt")
    B = load_matrix_from_file("../App/matrix_B.txt")
    save_multiply_matrices_to_file(A, B, "../App/multiplication_result.txt")

app()