import sys

from graph import Graph

import tree_min


def verify_local_min(g, u):
    """ Determines if the given vertex in the given graph is a local minimum.
        Returns true if so and false otherwise.

        g -- a complete binary tree as an undirected graph
        u -- the index of a vertex in g
    """
    n = g.size()

    if u < 0 or u >= n:
        # invalid vertex index
        return False

    for v in g.edges(u):
        if g.value(v) < g.value(u):
            # neighbor v has value less than u
            return False

    return True


def read_input():
    """ Reads specification of a complete binary tree from standard input.
        The specification gives the number of levels on the first line, and
        the ordering of the vertices on the second.  Vertices are given
        starting with the root vertex and proceeding down level-by-level
        and left-to-right within levels.
    """
    # read number of levels
    levels = int(sys.stdin.readline())
    if levels <= 0:
        raise ValueError(f"number of levels must be nonnegative; got {levels}")

    # compute number of vertices
    n = (1 << levels) - 1

    # read permutation of vertices
    perm = [int(v) for v in sys.stdin.readline().split()]
    if len(perm) != n:
        raise ValueError(f"permutation of vertices must be {n} long; got {len(perm)}")
    
    # check that vertices are all given
    pos = [None for v in range(n)]
    for i, v in enumerate(perm):
        if v < 0 or v >= n:
            raise ValueError(f"invalid vertex index {v}")
        pos[v] = i
    if sum((1 if p is None else 0) for p in pos) > 0:
        raise ValueError(f"permutation missing {[v for v in range(n) if pos[v] is None]}")

    # read values of vertices in order given (root to leaves)
    shuffled_values = [float(v) for v in sys.stdin.readline().split()]
    if len(shuffled_values) != n:
        raise ValueError(f"need values for {n} vertices; got {len(shuffled_values)}")
    # put values in array in order of vertex index
    values = [None] * n
    for i, val in enumerate(shuffled_values):
        values[perm[i]] = val
    
    # build the graph
    g = Graph(n, values)
    for l in range(levels - 1):
        for v in range((1 << l) - 1, (1 << (l + 1)) - 1):
            # parent is vertex at index v in permutation is; children are at 2v+1 and 2v+2
            g.add_edge(perm[v], perm[2 * v + 1])
            g.add_edge(perm[v], perm[2 * v + 2])

    return g


def main():
    g = read_input()

    min_vert, min_value = tree_min.find_min_in_tree(g)
    if min_vert < 0 or min_vert >= g.size():
        print(f"invalid vertex index {min_vert}")
        return
    if min_value != g.value(min_vert):
        print(f"vertex {min_vert} value is {g.value(min_vert)}, not {min_value}")
        return
    if not verify_local_min(g, min_vert):
        print(f"vertex {min_vert} is not a local minimum")
        return
    print(min_value)

    
if __name__ == "__main__":
    main()
    
