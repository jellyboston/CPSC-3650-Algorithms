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
            r_dest, c_dest = r + p_r, c + p_c
            # guard OOB neighbors
            if 0 <= r_dest < rows and 0 <= c_dest < cols: 
                test_val = grid[r_dest][c_dest]
                if test_val < candidate_val: # we found a smaller neighbor
                    return False
        return True
    
    '''
    recursing on subgrid effectively resets pointer to (0,0), but we need
    to keep track of original grid indices for testing neighbors w.r.t full grid.
    We use these two as global indices: 

    r0 - row offset that if added would map to original grid row
    c0 - col fofset that if added would map to original grid col
    '''
    def split_min(split_grid, r0, c0, split_on_cols=True):
        # base case: small Hx2 subgrid (height doesn't shrink so idc)
        rows, cols = len(split_grid), len(split_grid[0])
        if cols <= 2 or rows <= 2:
            # search each cell for local min
            for r in range(rows):
                for c in range(cols):
                    if is_local_min(grid, r0 + r, c0 + c) == True:
                        return grid[r0 + r][c0 + c]
                    
        # recursive case: repeat split logic down the middle
        if split_on_cols:
            # column split
            split = cols // 2
            min_row, min_val = 0, float('inf')
            for r in range(rows):
                val = split_grid[r][split]
                if val < min_val:
                    min_row, min_val = r, val
            # decide whether to conquer l or r subgraph (prevent OOB)
            left_val = split_grid[min_row][split - 1] if split - 1 >= 0 else float('inf')
            right_val = split_grid[min_row][split + 1] if split + 1 < cols else float ('inf')

            # check if min_val candidate itself is a local min
            if is_local_min(grid, r0 + min_row, c0 + split) == True:
                return min_val
            # recurse on the left
            elif left_val <= right_val:
                # list comprehension -> row[:split] represents the cols we pick
                split_grid_left = [row[:split] for row in split_grid]
                return split_min(split_grid_left, r0, c0, split_on_cols=False)
            # recurse on the right
            else:
                split_grid_right = [row[split+1:] for row in split_grid]
                return split_min(split_grid_right, r0, c0 + split + 1, split_on_cols=False)
        else:
            # row split
            split = rows // 2
            min_col, min_val = 0, float('inf')
            for c in range(cols):
                val = split_grid[split][c]
                if val < min_val:
                    min_col, min_val = c, val
            # decide whether to conquer up or down subgraph (prevent OOB)
            up_val = split_grid[split - 1][min_col] if split - 1 >= 0 else float('inf')
            down_val = split_grid[split + 1][min_col] if split + 1 < rows else float('inf')

            # check if min_val candidate itself is a local min
            if is_local_min(grid, r0 + split, c0 + min_col) == True:
                return min_val
            # recurse on the top
            elif up_val <= down_val:
                # slice rows -> split_grid[:split] represents the rows we pick
                split_grid_top = split_grid[:split]
                return split_min(split_grid_top, r0, c0, split_on_cols=True)
            # recurse on the bottom
            else:
                split_grid_bottom = split_grid[split+1:]
                return split_min(split_grid_bottom, r0 + split + 1, c0, split_on_cols=True)

    '''
    Divide and conquer:
    - Divide: Split grid down the middle and search for min
    - Conquer: Recurse across smaller neighbor until base case is hit
        - Base Case: Kx2 grid where we can check directly for local min
    - Combine: return value (no merge)
    '''
    # YOUR SOLUTION HERE
    return split_min(grid, 0, 0)