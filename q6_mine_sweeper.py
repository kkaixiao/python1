def mine_sweeper(bombs, num_rows, num_cols):
    # NOTE: field = [[0] * num_cols] * num_rows would not work
    # because you need to create a new list for every row,
    # instead of copying the same list.
    field = [[0 for i in range(num_cols)] for j in range(num_rows)]
    for bomb_loc in bombs:
        field[bomb_loc[0]][bomb_loc[1]] = -1

    neighbors = []

    for bom_loc in bombs:
        for x in range(bom_loc[0] - 1, bom_loc[0] + 2):
            for y in range(bom_loc[1]-1, bom_loc[1] + 2):
                if (x > -1 and x < num_rows) and ( y > -1 and y < num_cols):
                    neighbors.append([x, y])

    for loc in neighbors:
        if loc not in bombs:
            field[loc[0]][loc[1]] += 1



    # first is row number, second is column number

    return field

print(mine_sweeper([[0, 0], [0, 1], [1, 2]], 3, 4))