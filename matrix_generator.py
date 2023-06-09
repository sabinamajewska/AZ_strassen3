import numpy


def matrix_generator(n):
    return numpy.random.randint(0, 100, (n, n))


def save_generated_matrix_to_file(n, filepath):
    A = matrix_generator(n)
    f = open(filepath, "w")
    for i in range(len(A)):
        f.write(' '.join(map(str, A[i])) + '\n')
    f.close()
    return


n = 10
save_generated_matrix_to_file(n, "Example/generated_matrix_1.txt")
save_generated_matrix_to_file(n, "Example/generated_matrix_2.txt")
