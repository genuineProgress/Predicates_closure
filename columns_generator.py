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

if __name__ == "__main__":
    columns = generate_columns(4)
    with open("columns_output.txt", "w") as f:
        f.write("All possible columns of size 4 consisting of elements 0, 1, 2:\n")
        transposed_columns = zip(*columns)
        for row in transposed_columns:
            for item in row:
                f.write(str(item) + " ")
            f.write("\n")