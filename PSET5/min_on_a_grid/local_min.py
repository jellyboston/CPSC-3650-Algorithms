import itertools as it

def find_min(grid):
    """ Finds a local minimum in the given 2-D array (list of lists) and returns
        its value.

        grid -- a rectangular 2-D array of numbers
    """
    def is_local_min(grid, r, c):
        # prime the loop
        rows, cols = len(grid), len(grid[0])
        candidate_val = grid[r][c]
        pivots = [(0,1), (0,-1), (1,0), (-1,0)]

        # test each pivot direction for other local mins
        for p_r, p_c in pivots:
            test_val = grid[r + p_r][c + p_c]
            if test_val < candidate_val: # we found a smaller neighbor
                return False
        return True
    
    def split_min(split_grid):
        # base case: small Kx2 subgrid (height doesn't shrink so idc)
        rows, cols = len(split_grid), len(split_grid[0])
        if cols <= 2:
            # search each cell for local min
            for r in range(rows):
                for c in range(cols):
                    if is_local_min(split_grid, r, c):
                        return split_grid[r][c]
                    
        # recursive case: repeat split logic down the middle
        split = cols // 2
        min_row, min_val = 0, float('inf')
        for r in range(rows):
            val = grid[r][split]
            if val < min_val:
                min_row, min_val = r, val
        # decide whether to conquer l or r subgraph (prevent OOB)
        left_val = grid[min_row][split - 1] if split - 1 >= 0 else float('inf')
        right_val = grid[min_row][split + 1] if split + 1 < cols else float ('inf')

        # base case: check if min_val candidate itself is a local min
        if is_local_min(grid, min_row, split) == True:
            return min_val
        # recurse on the left
        elif left_val <= right_val:
            split_grid = grid[0:rows-1][0:split-1]
            return split_min(split_grid)
        # recurse on the right
        else:
            split_grid = grid[0:rows-1][split+1:cols-1]
            return split_min(split_grid)

    '''
    Divide and conquer:
    - Divide: Split grid down the middle and search for min
    - Conquer: Recurse across smaller neighbor until base case is hit
        - Base Case: 2x2 grid where we can check directly for local min
    - Combine: return value (no merge)
    
    '''
    # YOUR SOLUTION HERE
    rows, cols = len(grid), len(grid[0])
    split = cols // 2

    # find candidate min in middle col
    min_row, min_val = 0, float('inf')
    for r in range(rows):
        val = grid[r][split]
        if val < min_val:
            min_row, min_val = r, val

    # decide whether to conquer l or r subgraph (prevent OOB)
    left_val = grid[min_row][split - 1] if split - 1 >= 0 else float('inf')
    right_val = grid[min_row][split + 1] if split + 1 < cols else float ('inf')

    # base case: check if min_val candidate itself is a local min
    if is_local_min(grid, min_row, split) == True:
        return min_val
    # recurse on the left
    elif left_val <= right_val:
        split_grid = grid[0:rows-1][0:split-1]
        return split_min(split_grid)
    # recurse on the right
    else:
        split_grid = grid[0:rows-1][split+1:cols-1]
        return split_min(split_grid)