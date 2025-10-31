import itertools as it

import worst_case_input

def validate_input(grid, h, w):
    """ Determines if the input is a rectangluar 2-D array (list of lists)
        of the given size with all elements being numbers.
        Throws an exception if not.

        grid -- anything
    """
    rows = len(grid)
    if rows != h:
        raise ValueError(f"grid height must be {h}; got {rows}")
    
    for r in range(rows):
        if len(grid[r]) != w:
            raise ValueError(f"grid rows must all have {w} columns; got {len(grid[r])}")
        for x in grid[r]:
            try:
                float(x)
            except:
                raise ValueError(f"elements must be numbers; got{x}")
    return


def hill_descent(grid, sr, sc):
    """ Finds a local minimum in a grid by hill descent.  Returns the minimum found
        and the number of steps to find it.  The initial probe counts as a step, so
        the number of steps returns eill always be at least 1.

        grid -- a rectangular array of numbers
        sr -- a valid row index into grid for the location to start from
        sc -- a valid column inde into grid for the loction to start from
    """
    directions = [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0)]
    
    def in_bounds(r, c):
        return r >= 0 and r < len(grid) and c >= 0 and c < len(grid[0])

    # start at given location
    row = sr
    col = sc

    # prime the loop and initialize counter
    step_dir = (0, 0)
    min_adj = grid[row][col] + 1
    steps = 0

    # loop until current location has min_value among adjacent locations
    while grid[row][col] != min_adj:
        # step in direction of minimum value
        row += step_dir[0]
        col += step_dir[1]

        # count one more step
        steps += 1

        # find minimum value among adjacent locations
        adjacent = ((grid[row + d[0]][col + d[1]], d) for i, d in enumerate(directions)
                                                      if in_bounds(row + d[0], col + d[1]))
        min_adj, step_dir = min(adjacent, key=lambda p: p[0])

    # return value of local minimum and the steps taken to find it
    return grid[row][col], steps


def main():
    h = 9
    w = 11
    lower_bound = (h * w) // 2
    
    # get student input
    grid = worst_case_input.make_grid(h, w)
    validate_input(grid, h, w)

    # make iterator over all edges
    #edges = it.chain(((r, 0) for r in range(len(grid))),
    #                 ((r, len(grid[0]) - 1) for r in range(len(grid))),
    #                 ((0, c) for c in range(1, len(grid[0]) - 1)),
    #                 ((len(grid) - 1, c) for c in range(1, len(grid[0]) - 1)))
    #max_steps = max(hill_descent(grid, r, c)[1] for r, c in edges)
    max_steps = max(hill_descent(grid, r, c)[1] for r in range(h) for c in range(w))

    if max_steps < lower_bound:
        print(f"max_steps only {max_steps}; require at least {lower_bound}")
    else:
        print(f"max_steps >= {lower_bound} as required")
                     

if __name__ == "__main__":
    main()
