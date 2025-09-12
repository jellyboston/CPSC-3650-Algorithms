"""
A wheel meets the following crtieria:
1. A hub with degree(v-1) exists
2. Every rim vertex is a neighbor to the hub
3. Every rim vertex is deg'(v) = 2 (minus the hub)
4. DFS yields a seen list of V-1 vertices => rim size is V-1
"""
def rim_dfs_visit(g, u, hub, visited):
    visited.add(u)
    for v in g.edges(u):
        if v == hub:
            continue
        if v not in visited:
            rim_dfs_visit(g, v, hub, visited)

def dfs_check_rim_size(g, hub):
    visited = set()

    # start should not be the hub
    for v in range(g.size()):
        if v != hub:
            rim_dfs_visit(g, v, hub, visited)
            break # only iterate once
    
    return len(visited)

def is_wheel(g):
    """ Returns True if g is a wheel and False otherwise.
        g -- an undirected graph with at least 5 vertices
    """
    # check condition 1
    hub = None
    hub_count = 0
    for v in range(g.size()): # O(V)
        if g.outdegree(v) == g.size() - 1:
            hub_count += 1
            hub = v
    if hub_count != 1: return False
    
    # check condition 2: every rim vertex is a neighbor to the hub
    for v in range(g.size()): # O(V)
        if v != hub:
            if not g.has_edge(v, hub): return False
    
    # check condition 3: every rim vertex is deg'(v) = 2 (minus the hub)
    for v in range(g.size()): # O(V)
        if v != hub:
            # compute degree if hub were removed
            induced_degree = len(g.edges(v)) - 1
            if induced_degree != 2: return False

    # check condition 4: seen list yields V-1 vertices
    if dfs_check_rim_size(g, hub) != g.size() - 1: # O(V+E)
        return False
    
    return True