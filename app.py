from Algoritms.load_and_safe_matrix import *


# INSTRUKCJA OBSŁUGI PROGRAMU
# Wpisz macierze, które chcesz pomnożyć, pierwszą macierz zapisz do pliku App/matrix_A.txt, a drugą do App/matrix_B.txt.
# Następnie uruchom plik app.py, wynik zostanie zapisany w pliku App/multiplication_result.txt


def app():
    A = load_matrix_from_file("App/matrix_A.txt")
    B = load_matrix_from_file("App/matrix_B.txt")
    save_multiply_matrices_to_file(A, B, "App/multiplication_result.txt")


app()
