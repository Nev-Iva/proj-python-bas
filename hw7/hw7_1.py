class Matrix:
    def __init__(self, matrix_list):
        self.matrix_list = matrix_list

    def __getitem__(self, num_pos):
        i, j = num_pos
        return self.matrix_list[i][j]

    def __str__(self):
        str_matrix = ''
        for row in self.matrix_list:
            for elem in row:
                str_matrix += '{:4d}'.format(elem)
            str_matrix += '\n'
        return str_matrix

    def __add__(self, other):
        for i in range(len(self.matrix_list)):
            for j in range(len(other.matrix_list[i])):
                self.matrix_list[i][j] = self.matrix_list[i][j] + other.matrix_list[i][j]
        return Matrix.__str__(self)


matrix_1 = Matrix([[-2, 3, 1], [-1, 2, 3], [2, 1, -1], [1, 3, -1]])
matrix_2 = Matrix([[-2, 1, 3], [-3, 1, 2], [0, 2, 0], [2, 2, -1]])
print(matrix_1)
print(matrix_2)
print(matrix_1.__add__(matrix_2))