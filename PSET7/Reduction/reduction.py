from graph import Graph

def reduce(g):
    """ Given a graph g, create a new graph g' such that
        an approximate Hamiltonian path in g' corresponds to a
        Hamiltonian path in g.

        g -- a graph
    """
    # YOUR SOLUTION HERE
    return Graph(g.size())
