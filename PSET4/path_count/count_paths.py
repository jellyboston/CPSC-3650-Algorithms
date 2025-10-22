import sys

from digraph import Digraph
import paths


def read_input():
    # read and check number of vertices
    n = int(sys.stdin.readline())
    if n <= 0:
        raise ValueError(f"Invalid number of vertices: {n}")
    g = Digraph(n)

    # read source
    source = int(sys.stdin.readline())
    if source < 0 or source >= n:
        raise ValueError(f"Invalid vertex index: {source}")
            
    # read one edge per line
    for line in sys.stdin:
        edge = line.split()
        if len(edge) != 2:
            raise ValueError(f"Invalid edge: {line}")
        u = int(edge[0])
        v = int(edge[1])
        if u < 0 or u >= n:
            raise ValueError(f"Invalid vertex index: {u}")
        if v < 0 or v >= n:
            raise ValueError(f"Invalid vertex index: {v}")
        g.add_edge(u, v)
    return g, source


def main():
    # read input
    g, source = read_input()
    
    # count paths and output result
    count = paths.count_paths_in_dag(g, source)
    print(count)
    

if __name__ == "__main__":
    main()