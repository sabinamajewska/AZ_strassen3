# import unittest
# from Algoritms.load_and_safe_matrix import *
# from Algoritms.functions import stand_mnoz, multiply_matrices_strassen
#
# A = load_matrix_from_file("Example/matrix_example_1.txt")
# B = load_matrix_from_file("Example/matrix_example_2.txt")
# stand_mnoz = stand_mnoz(A, B)
#
#
# class MyTestCase(unittest.TestCase):
#
#     def test_stand_mnoz_is_equal_multiply_matrices_strassen(self):
#         # given
#         A = load_matrix_from_file("Example/matrix_example_1.txt")
#         B = load_matrix_from_file("Example/matrix_example_2.txt")
#         # when
#         strassen = multiply_matrices_strassen(A, B)
#         # then
#         self.assertEqual(strassen, stand_mnoz)
