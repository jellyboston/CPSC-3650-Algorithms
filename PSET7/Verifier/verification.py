def verify(g, path):
    """ Given a graph G and a path P, return True if P
        is an approximate Hamiltonian path and False otherwise

        g -- a graph
        path -- a path in g represented as a list of vertices
    """
    # YOUR SOLUTION HERE
    # enforce valid path (w/ adjacency check)
    # for idx in range(len(path) - 1):
    #     u = path[idx]
    #     v = path[idx+1]
    #     if not g.has_edge(u, v):
    #         return False # path has invalid edge
    
    
    '''
    APPROX-HP invariant:
    1. visits |v| - 1 vertices once
    2. visits remaining vertex **at least once** (>= ok)
    3. does not traverse any edge more than once
    '''
    # check vertex constraints
    count_vertex = [0] * g.size()
    for v in path:
        # edge case: invalid vertex
        if v < 0 or v >= g.size():
            return False
        count_vertex[v] += 1
    num_single = 0
    for idx, count in enumerate(count_vertex):
        if count == 0:
            # vertex not visited
            return False
        if count == 1:
            num_single += 1
    if num_single < g.size() - 1:
        return False

    # check edge constraints
    used_edges = []
    for idx in range(len(path) - 1):
        u = path[idx]
        v = path[idx+1]
        edge = (min(u, v), max(u, v)) # normalize since undirected
        if edge in used_edges:
            return False
        else:
            used_edges.append(edge)
            
    return True
