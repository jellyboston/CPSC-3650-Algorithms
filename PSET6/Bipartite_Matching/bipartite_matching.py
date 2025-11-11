import sys
import random
import itertools as it

from graph import Graph
import reduction
import flow

def read_graph():
    # read and check number of left vertices and right vertices
    n = int(sys.stdin.readline())
    if n <= 0:
        raise ValueError(f"Invalid number of vertices: {n}")
    m = int(sys.stdin.readline())
    if m <= 0:
        raise ValueError(f"Invalid number of vertices: {m}")
    g = Graph(n + m)

    # read one edge per line
    for line in sys.stdin:
        ends = line.split()
        if len(ends) != 2:
            raise ValueError(f"Invalid edge: {line}")
        u = int(ends[0])
        v = int(ends[1])
        if u < 0 or u >= n:
            raise ValueError(f"Invalid from index: {u}")
        if v < n or v >= n + m:
            raise ValueError(f"Invalid to index: {v}")
        g.add_edge(u, v)
    return g, n, m


def main():
    g, n, m = read_graph()
    
    # reduce problem to maximum flow problem
    g_prime, source, sink = reduction.bipartite_to_flow(g, n, m)

    # find maximum flow in transformed graph
    flow.ford_fulkerson(g_prime, source, sink)

    # extract matching from flow
    matching = reduction.flow_to_matching(g_prime, source, sink, n, m)

    # verify that matching is valid
    degree = [0] * (n + m)
    for u, v in matching:
        if not isinstance(u, int):
            raise ValueError(f"vertex {u} in matching is not an int")
        if not isinstance(v, int):
            raise ValueError(f"vertex {v} in matching is not an int")
        if u < 0 or u > n + m:
            raise ValueError(f"invalid vertex index {u}")
        if v < 0 or v > n + m:
            raise ValueError(f"invalid vertex index {v}")

        degree[u] += 1
        if degree[u] > 1:
            raise ValueError(f"{u} appears in multiple edges in matching")
        
        degree[v] += 1
        if degree[v] > 1:
            raise ValueError(f"{v} appears in multiple edges in matching")
    
    # output size for autograder framework to check against expected
    print(len(matching))


if __name__ == "__main__":
    main()
