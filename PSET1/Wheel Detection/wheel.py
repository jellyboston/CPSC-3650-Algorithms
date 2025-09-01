"""
A wheel meets the following crtieria:
1. A hub with degree(v-1) exists
2. Every rim vertex is a neighbor to the hub
3. Every rim vertex is deg'(v) = 2 (minus the hub)
4. DFS yields a seen list of V-1 vertices
"""
def rim_dfs_visit(g, u, results, hub, visited, is_hub_neighbor):
    results[u].color = 1 # processing
    visited.add(u)
    for v in g._adj[u]:
        if v == hub:
            is_hub_neighbor = True
            continue
        if results[v].color == 0:
            results[v].parent = u
            rim_dfs_visit(g, v, results, hub, visited)
    
    results[u].color = 2 # finished

def check_wheel_rim_dfs(g, hub):
    visited = set()
    results = [DFSResult() for i in range(g._size)]
    is_hub_neighbor = False

    # start should not be the hub
    for v in g:
        if v == hub:
            continue
        if results[v].color == 0: 
            rim_dfs_visit(g, v, results, hub, visited, is_hub_neighbor)
    
    # check condition 2
    if not is_hub_neighbor:
        return False
    # check condition 4
    if len(visited) != g._size - 1:
        return False
    # check condition 3
    for v in visited:
        if g.degree(g, v) != 2:
            return False
    return True

def is_wheel(g):
    """ Returns True if g is a wheel and False otherwise.
        g -- an undirected graph with at least 5 vertices
    """
    hub = None

    # first check
    for v in g:
        if g.degree(g, v) == g._size - 1:
            hub = v
    if hub is None:
        return False
    

    # begin DFS
    return check_wheel_rim_dfs(g, hub)
