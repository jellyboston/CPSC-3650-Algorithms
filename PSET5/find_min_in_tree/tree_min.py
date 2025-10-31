def find_min_in_tree(g):
    """ Returns the index of a vertex that is a local minimum in the given graph and its value.

        g -- a complete binary tree as an undirected graph
    """
    # YOUR SOLUTION HERE
    '''
    Pseudocode
    divide: conceptually separate graph into one smaller subtree
    conquer: recurse into subtree until local min is found and return
    '''
    def recursive_min(vertex, parent):
        # get all neighbors
        nbrs = [u for u in g.edges(vertex) if u != parent]

        # base case: found the local minimum
        local_min = True
        for c in nbrs:
            if g.value(vertex) > g.value(c):
                local_min = False
                break
        if local_min:
            return vertex
        
        # recurse onto the smallest neighbor
        candidate = vertex
        for c in nbrs:
            if g.value(c) < g.value(candidate):
                candidate = c
        if nbrs and g.value(candidate) < g.value(vertex):
                return recursive_min(candidate, vertex)
        
        # handle plateau
        return vertex
        
    if g.size() == 1:
        return 0, g.value(0)
    
    # pick any start vertex
    start = 0
    min_index = recursive_min(start, None)
    return min_index, g.value(min_index)
