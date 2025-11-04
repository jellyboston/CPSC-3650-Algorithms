def make_grid(h, w):
    """ Returns an h-row, w-column 2-D array (list of lists) of numbers.

        h -- 9
        w -- 11
    """
    '''
    Function holds that: 
     - Algorithm will step column-wise in a snake pattern
     - Each next cell stepped to is strictly smaller than the current
     - Every odd row contains a barrier with ints strictly larger than both adj.
       snake cells
     - All non-barrier cells are smaller than those orthogonal to it
     - Start is (0,0) and stop point (10, 8) is the local min with 49 steps exactly
    '''
    # hint: keep things linked up with all 2-digit integers
    # use +n or -n for single-digit values
    # values needn't be unique
    # YOUR SOLUTION HERE

    # start: create 2D arr with arbitrarily large values (barrier rows)
    BARRIER_VALUE = 999
    grid = [[BARRIER_VALUE for _ in range(w)] for _ in range(h)]

    # prime the loop
    snake_rows = list(range(0, h, 2)) # path down only even rows
    start_val = h * w # 99

    # iterate in snake pattern and overwrite with strictly decreasing vals
    '''
    Each iteration writes: "l-r + drop + r-l + drop" 
    i = 0 -> writes rows 0 and 2
    i = 2 -> writes rows 4 and 6
    i = 4 -> writes row 8 (terminates)
    '''
    for row in range(0, len(snake_rows), 2):
        # iterate left -> right
        for col in range(w):
            grid[row][col] = start_val
            start_val =- 1
        
        # drop only if not OOB (right side of grid)
        if row + 1 < len(snake_rows):
            for drop_row in range(2):
                 grid[drop_row][len(snake_rows)] = start_val
                 start_val =- 1
        
        # right -> left only if not OOB
        if row + 1 < len(snake_rows):
            for col in range(w-1, -1, -1):
                grid[row + 2][col] = start_val
                start_val =- 1

        # again drop (left side of grid)
        if row + 1 < len(snake_rows):
            for drop_row in range(2, 4): # draw this out it makes sense
                grid[drop_row][0] = start_val
                start_val =- 1

    return grid
