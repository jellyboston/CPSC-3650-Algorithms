def count_paths_in_dag(g, source):
    """ Computes and returns the number of paths that start from the
        given vertex in the given directed acyclic graph.

        g -- a directed, acyclic graph
        source -- the index of a vertex in g
    """
    # YOUR SOLUTION HERE
    # topological sort: sort by descending f 
    dfs = g.dfs()
    top_order = [idx # list comprehension 101: collect only vertex indices
                 for idx, result in sorted(enumerate(dfs), # (0, dfs[0]), ... (idx, dfs[idx])
                                          key=lambda x: x[1].f,  # extract f = dfs[x].f
                                          reverse=True)]  
    count = [0] * g.size() # running total of path count
    count[source] = 1
    for u in top_order: 
        # assume topological sort: ancestors of the source won't be counted
        for v in g.edges(u):
            count[v] += count[u]
    return sum(count)