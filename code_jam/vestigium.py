import numpy as np

# input of test cases
test_cases = int(input().strip())

for case in range(test_cases):

    trace = rrow = rcol = 0
    # input matrix size
    matrix_size = int(input().strip())
    array = np.zeros((matrix_size, matrix_size), int)
    # filling array
    for i in range(matrix_size):
        array[i] = input().strip().split()

    # Solution
    for index in range(matrix_size):
        # calculating trace
        trace += array[index][index]
        # calculating repeating row
        row_set = set(array[index])

        if len(row_set) < matrix_size:
            rrow += 1
        # calculating repeating column
        col_set = set(array[:, index])
        if len(col_set) < matrix_size:
            rcol += 1

    print("Case #{}: {} {} {}".format(case+1, trace, rrow, rcol))
