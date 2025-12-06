import sys
import random
import itertools as it

from graph import Graph
import verification


def read_graph():
    # read and check number of vertices
    n = int(sys.stdin.readline())
    g = Graph(n)

    p = list(sys.stdin.readline().split())
    p = [int(v) for v in p]

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
    return g, p

def main():
    g, p = read_graph()
    
    # check wheel-ness
    print(verification.verify(g, p))


if __name__ == "__main__":
    main()
