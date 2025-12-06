from graph import Graph

def reduce(g):
    """ Given a graph g, create a new graph g' such that
        an approximate Hamiltonian path in g' corresponds to a
        Hamiltonian path in g.

        g -- a graph
    """
    # YOUR SOLUTION HERE
    # 1. Read g’s size and edges
    size = g.size()

    # 2. Create a new graph gprime with n + (constant) vertices
    REDUCTION_VERTS = 1 # single source and dest node
    gprime = Graph(size + REDUCTION_VERTS)

    # 3. Copy/transform all original vertices and edges into gprime (use same indices as original)
    for u in range(g.size()):
        if u == 0:
            # connect to start node in reduction
            R_VERTEX = gprime.size() - 1
            gprime.add_edge(u, R_VERTEX)
        for v in g.edges(u):
            # normalize edges
            gprime.add_edge(min(u, v), max(u, v))

    return gprime