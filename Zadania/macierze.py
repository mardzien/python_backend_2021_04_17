import pytest
from itertools import zip_longest

matrix1 = [[1, -2], [-3, 4]]
matrix2 = [[2, -1], [0, -1]]


def add_mat(mat1, mat2):
    result = []

    for row1, row2 in zip(mat1, mat2):
        temp_row = []
        for e1, e2 in zip(row1, row2):
            temp_row.append(e1 + e2)
        result.append(temp_row)

    return result


print(add_mat(matrix1, matrix2))


def add_mat2(*args):
    result = []
    for rows in zip(*args):

        temp_row = []
        # print(rows)
        for elements in zip(*rows):
            # print(elements)
            temp_row.append(sum(elements))
        result.append(temp_row)

    return result


matrix3 = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]
matrix4 = [[1, 1, 0], [1, -2, 3], [-2, 2, -2]]


def check_size(m):
    n_rows = len(m)
    n_cols = len(m[0])

    for row in m:
        if len(row) != n_cols:
            raise ValueError("Every row should have same number of columns")


def add_mat3(*args):

    # sizes = set()

    result = []
    try:
        for rows in zip_longest(*args, fillvalue='?'):
            temp_row = []
            # print(rows)
            for elements in zip_longest(*rows, fillvalue='?'):
                # print(elements)
                temp_row.append(sum(elements))
            result.append(temp_row)
    except:
        raise ValueError("Given matrices are not the same size.")

    return result


# matrix3 = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]
# matrix4 = [[1, 1, 0], [1, -2, 3], [-2, 2]]
#
# print(add_mat3(matrix3, matrix4))


def test_add():
    assert add_mat([[1, -2], [-3, 4]], [[2, -1], [0, -1]]) == [[3, -3], [-3, 3]]
    assert add_mat2([[1, 9], [7, 3]], [[5, -4], [3, 3]], [[2, 3], [-3, 1]]) == [[8, 8], [7, 7]]


def test_add_raises_exceptions():
    with pytest.raises(ValueError):
        add_mat3([[1, 9], [7, 3]], [[1, 2], [3]])
