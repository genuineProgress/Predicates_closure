import function_def as f
import itertools
import functools
# below function was needed once in the past check
def check_fs(data):  # return 0 if check is not successful and 1 otherwise
    # here we check f_3
    counter=0
    # check_f_3=1
    # for list in data:
    #     set_list=set(list)
    #     n = len(list)
    #     x = itertools.product(set_list, repeat=4)
    #     set_list2 = set(map(lambda y: tuple(f_3(*a) for a in zip(*y)), x))
    #     set_list = set_list.union(set_list2)
    #     #for tup in data:
    #         #print(tup)
    #     # print()
    #     if len(set_list) != n:
    #         check_f_3=0
    #     else:
    #         counter+=1
    #         print(list)
            #print(list)
    #if(check_f_3==0): return 0
    #here we check f_4
    check_f_4=1
    for list in data:

        set_list=set(list)
        n = len(set_list)
        x = itertools.product(set_list, repeat=5)
        set_list2 = set(map(lambda y: tuple(f.f_4(*a) for a in zip(*y)), x))
        set_list = set_list.union(set_list2)
        for tup in set_list2:
            print(tup)
        # for tup in data:
        #    print(tup)
        # print()
        if len(set_list) != n:
            check_f_4=0
            print(list)
    if(check_f_4==0): return 0
    # # #here we check f_5
    # check_f_5 = 1
    # for list in data:
    #     set_list = set(list)
    #     n = len(list)
    #     x = itertools.product(set_list, repeat=6)
    #     set_list2 = set(map(lambda y: tuple(f_5(*a) for a in zip(*y)), x))
    #     set_list = set_list.union(set_list2)
        # for tup in data:
        #    print(tup)
        # print()
        # if len(set_list) != n:
        #     check_f_5=0
        #     print(list)
    # if(check_f_5==0): return 0
    if (#check_f_3==0
             #or
             check_f_4==0# or check_f_5 == 0
            ):
        return 0
    else:
        return 1
#prints tuple without parentheses and commas
def printx(tup):
    print(' '.join(str(item) for item in tup))
    return
#used to read matrix as list of lists
def read_matrix_from_file(file_path):
    matrix = []
    with open(file_path, 'r') as file:
        for line in file:
            row = list(map(int, line.strip().split()))
            matrix.append(row)
    return matrix
#used to transpose matrix as list of lists
def transpose_matrix(matrix):
    # Use the zip function to transpose the matrix
    transposed_matrix = list(zip(*matrix))
    return transposed_matrix
#used to write matrix in an ordinary way
def write_matrix_to_file(matrix, file_path):
    with open(file_path, 'w') as file:
        for row in matrix:
            file.write(' '.join(map(str, row)) + '\n')
def generate_columns(size):
    if size <= 0:
        return [[]]
    smaller_columns = generate_columns(size - 1)
    columns = []
    for col in smaller_columns:
        for num in range(2):
            new_col = col + [num]
            columns.append(new_col)
    return columns
