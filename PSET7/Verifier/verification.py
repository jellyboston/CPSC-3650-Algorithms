def verify(g, path):
    """ Given a graph G and a path P, return True if P
        is an approximate Hamiltonian path and False otherwise

        g -- a graph
        path -- a path in g represented as a list of vertices
    """
    # YOUR SOLUTION HERE
    # enforce valid path (w/ adjacency check)
    for idx in range(len(path) - 1):
        u = path[idx]
        v = path[idx+1]
        if not g.has_edge(u, v):
            return False # path has invalid edge
    
    '''
    APPROX-HP invariant:
    1. visits |v| - 1 vertices once
    2. visits remaining vertex **at least once** (>= ok)
    3. does not traverse any edge more than once
    '''
    count_vertex = [0] * g.size()
    for v in path:
        count_vertex[v] += 1
    # verify
    remaining_vertex = -1
    found = False
    for v in count_vertex:
        # if some other vertex is visited multiple times
        if v != remaining_vertex and found and count_vertex[v] >= 2:
            return False
        elif count_vertex[v] >= 2:
            found = True
            remaining_vertex = v
        else:
            continue
    
    return False
