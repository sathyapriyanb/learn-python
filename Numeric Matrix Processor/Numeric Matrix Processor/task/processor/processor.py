import math


def main():
    while True:
        print('1. Add matrices', '2. Multiply matrix by a constant', '3. Multiply matrices', '4. Transpose matrix',
              '5. Calculate a determinant', '6. Inverse matrix', '0. Exit', sep='\n')
        state = int(input('Your choice:'))
        if state == 1:
            add()
        elif state == 2:
            scalar_mul()
        elif state == 3:
            mul()
        elif state == 4:
            trans()
        elif state == 5:
            det()
        elif state == 6:
            inverse()
        elif state == 0:
            break
        print()


def print_result(value):
    if value:
        print('The result is:')
        if isinstance(value, list):
            [print(*oneSet) for oneSet in value]
        else:
            print(value)


def add():
    a, a_col, a_row, b, b_col, b_row = get_two_matrix()
    print_result(calc_add(a, a_col, a_row, b, b_col, b_row))


def get_two_matrix():
    a_row, a_col = [int(i) for i in input('Enter size of first matrix:').split()]
    print('Enter first matrix:')
    a = [[float(i) for i in input().split()] for _ in range(a_row)]
    b_row, b_col = [int(i) for i in input('Enter size of second matrix:').split()]
    print('Enter second matrix:')
    b = [[float(i) for i in input().split()] for _ in range(b_row)]
    return a, a_col, a_row, b, b_col, b_row


def calc_add(a, a_col, a_row, b, b_col, b_row):
    if a_row != b_row or a_col != b_col:
        print("The operation cannot be performed.")
        return None
    else:
        return [[a[i][j] + b[i][j] for j in range(a_col)] for i in range(a_row)]


def scalar_mul():
    a, a_col, a_row = get_one_matrix()
    num = float(input('Enter constant:'))
    print_result(calc_scalar_mul(a, a_col, a_row, num))


def get_one_matrix():
    a_row, a_col = [int(i) for i in input('Enter size of matrix:').split()]
    print('Enter matrix:')
    a = [[float(i) for i in input().split()] for _ in range(a_row)]
    return a, a_col, a_row


def calc_scalar_mul(a, a_col, a_row, num):
    return [[a[i][j] * num for j in range(a_col)] for i in range(a_row)]


def mul():
    a, a_col, a_row, b, b_col, b_row = get_two_matrix()
    print_result(calc_mul(a, a_col, a_row, b, b_col, b_row))


def calc_mul(a, a_col, a_row, b, b_col, b_row):
    if a_col != b_row:
        print("The operation cannot be performed.")
        return None
    else:
        d = []
        for i in range(a_row):
            row = []
            for j in range(b_col):
                val = 0
                for k in range(a_col):
                    val += a[i][k] * b[k][j]
                row.append(val)
            d.append(row)
        return d


def trans():
    print('1. Main diagonal', '2. Side diagonal', '3. Vertical line', '4. Horizontal line', sep='\n')
    choice = int(input('Your choice:'))
    a, a_col, a_row = get_one_matrix()
    print_result(calc_trans(a, a_col, a_row, choice))


def calc_trans(a, a_col, a_row, choice):
    d = []
    if choice == 1:
        d = [[a[i][j] for i in range(a_row)] for j in range(a_col)]
    elif choice == 2:
        d = [[a[i][j] for i in range(a_row - 1, -1, -1)] for j in range(a_col - 1, -1, -1)]
    elif choice == 3:
        for i in range(a_row):
            a[i].reverse()
        d = a
    elif choice == 4:
        a.reverse()
        d = a
    return d


def det():
    a, a_row, a_col = get_matrix()
    print_result(calc_det(a))


def get_matrix():
    a_row, a_col = [int(i) for i in input('Enter matrix size:').split()]
    print('Enter matrix:')
    a = [[float(i) for i in input().split()] for _ in range(a_row)]
    return a, a_col, a_row


def calc_det(arr):
    value = 0
    row_len = len(arr)
    col_len = len(arr[0])
    if row_len == 1 and col_len == 1:
        return arr[0][0]
    elif row_len == 2 and col_len == 2:
        return arr[0][0] * arr[1][1] - arr[1][0] * arr[0][1]
    else:
        for i in range(0, col_len):
            m = [[arr[k][j] for j in range(0, row_len) if j != i] for k in range(1, row_len)]
            value += cofactor(1, i + 1) * arr[0][i] * calc_det(m)
    return value


def cofactor(i, j):
    return math.pow(-1, i + j)


def inverse():
    a, a_row, a_col = get_matrix()
    dete = calc_det(a)
    if dete == 0:
        print("This matrix doesn't have an inverse.")
    else:
        adj_val = adj(a, a_row, a_col)
        print_result(calc_scalar_mul(adj_val, a_col, a_row, 1 / dete))


def adj(arr, a_row, a_col):
    adj_val = [
        [cofactor(i, j) * calc_det([[arr[k][l] for l in list(range(a_col)) if l != j] for k in range(a_row) if k != i])
         for j in
         range(a_col)]
        for i in range(a_row)]
    return calc_trans(adj_val, a_col, a_row, 1)


if __name__ == '__main__':
    main()
