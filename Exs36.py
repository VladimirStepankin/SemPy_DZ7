def print_operation_table(operation, num_rows=9, num_columns=9):
    for x in range(1, num_rows + 1):
        for y in range(1, num_columns + 1):
            if num_columns == y:
                print(operation(x, y))
            else:
                print(operation(x, y), '\t', end='')


print_operation_table(lambda x, y: x * y)
