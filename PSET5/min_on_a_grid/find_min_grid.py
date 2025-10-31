import sys

import local_min

def main():
    # read dimensions
    h = int(sys.stdin.readline())
    w = int(sys.stdin.readline())

    if h <= 0:
        raise ValueError(f"height must be positive; got {h}")
    if w <= 0:
        raise ValueError(f"width must be positive; got {w}")

    grid = []
    for r in range(h):
        line = sys.stdin.readline()
        elts = line.split()
        if len(grid) > 0 and len(elts) != len(grid[0]):
            raise ValueError(f"all rows must have same size; got {line}")
        grid.append([float(x) for x in line.split()])

    print(local_min.find_min(grid))

if __name__ == "__main__":
    main()
    
