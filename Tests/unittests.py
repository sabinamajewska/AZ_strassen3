import unittest
from Algoritms.load_and_safe_matrix import *
from Algoritms.functions import stand_multiplycation, multiply_matrices_strassen
from Algoritms.matrix_generator import matrix_generator


class MyTestCase(unittest.TestCase):

    # adjust_size
    def test_adjust_size1(self):
        # given
        A = matrix_generator(81)
        expected_size = 81
        # when
        size = len(adjust_size(A))
        # then
        self.assertEqual(expected_size, size)

    def test_adjust_size2(self):
        # given
        A = matrix_generator(1)
        expected_size = 1
        # when
        size = len(adjust_size(A))
        # then
        self.assertEqual(expected_size, size)

    def test_adjust_size3(self):
        # given
        A = matrix_generator(100)
        expected_size = 243
        # when
        size = len(adjust_size(A))
        # then
        self.assertEqual(expected_size, size)

    # split
    def test_split1(self):
        # given
        A = matrix([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
        expected_result = (matrix([[1]]), matrix([[2]]), matrix([[3]]), matrix([[1]]), matrix([[2]]),
                           matrix([[3]]), matrix([[1]]), matrix([[2]]), matrix([[3]]))
        # when
        result = split(A)
        # then
        self.assertEqual(expected_result, result)

    def test_split2(self):
        # given
        A = matrix([[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18], [19, 20, 21, 22, 23, 24],
                    [25, 26, 27, 28, 29, 30], [31, 32, 33, 34, 35, 36]])
        expected_result = (matrix([[1, 2], [7, 8]]), matrix([[3, 4], [9, 10]]), matrix([[5, 6], [11, 12]]),
                           matrix([[13, 14], [19, 20]]), matrix([[15, 16], [21, 22]]), matrix([[17, 18], [23, 24]]),
                           matrix([[25, 26], [31, 32]]), matrix([[27, 28], [33, 34]]), matrix([[29, 30], [35, 36]]))
        # when
        result = split(A)
        # then
        self.assertTrue(np.array_equal(expected_result, result))

    # stand_multiplycation == myltiply_matrices_strassen
    def test_stand_multiplycation_is_equal_multiply_matrices_strassen1(self):
        # given
        A = load_matrix_from_file("../Example/matrix_example_1.txt")
        B = load_matrix_from_file("../Example/matrix_example_2.txt")
        stand = stand_multiplycation(A, B)
        # when
        strass = multiply_matrices_strassen(A, B)
        # then
        self.assertTrue(np.array_equal(stand, strass))

    def test_stand_multiplycation_is_equal_multiply_matrices_strassen2(self):
        # given
        A = matrix_generator(40)
        B = matrix_generator(40)
        stand = stand_multiplycation(A, B)
        # when
        strass = multiply_matrices_strassen(A, B)
        # then
        self.assertTrue(np.array_equal(stand, strass))

    def test_stand_multiplycation_is_equal_multiply_matrices_strassen3(self):
        # given
        A = matrix([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
        B = matrix([[8, 10, 20], [0, 0, 1], [5, 0, 200]])
        stand = stand_multiplycation(A, B)
        # when
        strass = multiply_matrices_strassen(A, B)
        # then
        self.assertTrue(np.array_equal(stand, strass))

    def test_stand_multiplycation_is_equal_multiply_matrices_strassen4(self):
        # given
        A = matrix_generator(100)
        B = matrix_generator(100)
        stand = stand_multiplycation(A, B)
        # when
        strass = multiply_matrices_strassen(A, B)
        # then
        self.assertTrue(np.array_equal(stand, strass))

    def test_stand_multiplycation_is_equal_multiply_matrices_strassen5(self):
        # given
        A = matrix([[105, 200, 453, 256], [781, 12, 93, 111], [101, 12, 433, 580], [49, 302, 114, 229]])
        B = matrix([[17, 1, 0, 5], [400, 507, 123, 123], [5, 0, 2, 7], [890, 671, 22, 432]])
        stand = stand_multiplycation(A, B)
        # when
        strass = multiply_matrices_strassen(A, B)
        # then
        self.assertTrue(np.array_equal(stand, strass))

    def test_stand_multiplycation_is_equal_multiply_matrices_strassen6(self):
        # given
        A = matrix_generator(27)
        B = matrix_generator(27)
        stand = stand_multiplycation(A, B)
        # when
        strass = multiply_matrices_strassen(A, B)
        # then
        self.assertTrue(np.array_equal(stand, strass))

    def test_stand_multiplycation_is_equal_multiply_matrices_strassen7(self):
        # given
        A = matrix([[5]])
        B = matrix([[48]])
        stand = stand_multiplycation(A, B)
        # when
        strass = multiply_matrices_strassen(A, B)
        # then
        self.assertTrue(np.array_equal(stand, strass))
