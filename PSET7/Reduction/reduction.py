from graph import Graph

def reduce(g):
    """ Given a graph g, create a new graph g' such that
        an approximate Hamiltonian path in g' corresponds to a
        Hamiltonian path in g.

        g -- a graph
    """
    # YOUR SOLUTION HERE
    size = g.size()

    # new graph gprime with n + one reduciton vertex
    '''
    Approach:
    - X shape reduction graph with three-clique bottom
    - assign edges w/ corner of reduction shape to all vertices in G
    '''
    REDUCTION_VERTS = 5
    gprime = Graph(size + REDUCTION_VERTS)

    # create reduction graph
    reduction_idx = gprime.size() - REDUCTION_VERTS
    # for vtx in range(reduction_idx, gprime.size):
    NODE1, NODE2 = reduction_idx, reduction_idx + 1
    FREE_VERT = reduction_idx + 2
    NODE4, NODE5 = reduction_idx + 3, reduction_idx + 4

    # add reduction graph edges (leave out repeated edges since undirected)
    # node1 edges
    gprime.add_edge(NODE1, NODE2)
    gprime.add_edge(NODE1, FREE_VERT)

    # node2 edges
    gprime.add_edge(NODE2, FREE_VERT)

    #node3 edges 
    gprime.add_edge(FREE_VERT, NODE4)
    gprime.add_edge(FREE_VERT, NODE5)

    # connect an edge with degree 1 to every vtx of original
    for v in range(size):
        gprime.add_edge(NODE5, v)

    # copy edges to gprime (use same indices as original)
    for u in range(size):
        for v in g.edges(u):
            # normalize edges
            gprime.add_edge(min(u, v), max(u, v))

    return gprime