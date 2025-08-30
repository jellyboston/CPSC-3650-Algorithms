import sys
import random
import itertools as it

from graph import Graph
import wheel


def read_graph():
    # read and check number of vertices
    n = int(sys.stdin.readline())
    if n <= 4:
        raise ValueError(f"Invalid number of vertices: {n}")
    g = Graph(n)

    # read one edge per line
    for line in sys.stdin:
        ends = line.split()
        if len(ends) != 2:
            raise ValueError(f"Invalid edge: {line}")
        u = int(ends[0])
        v = int(ends[1])
        if u < 0 or u >= n:
            raise ValueError(f"Invalid vertex index: {u}")
        if v < 0 or v >= n:
            raise ValueError(f"Invalid vertex index: {v}")
        g.add_edge(u, v)
    return g

def main():
    g = read_graph()
    
    # check wheel-ness
    print(wheel.is_wheel(g))


if __name__ == "__main__":
    main()
