import random

from digraph import Digraph

'''
Kosaraju's Algorithm:
1. Run DFS
2. Reverse every edge in the graph
3. Run DFS while no unseen

'''
def transpose_graph(g):
    # New transpose graph that stores rev. edges
    reversed_graph = Digraph(g.size)
    for v in range(g.size):
        v_edges = g.edges(v)
        for e in v_edges: # 1D array
            reversed_graph.add_edge(e, v)
    return reversed_graph

def reset_color(og_ordering):
    for result in og_ordering:
        result.color = 0

'''
Returns:
    list: vertex ids sorted by descending finished time
'''
def extract_reverse_order(og_ordering, g):
    assert g.size() == len(og_ordering), "use interchangeably"
    reverse = []
    for v in range(g.size):
        assert og_ordering[v].finish != None
        reverse[v] = (og_ordering[v].finish, v)
    reverse.sort(reverse=True) # sorts descending by first element (finish)
    new_order = [v for f, v in reverse]
    return new_order

'''
Return:
    list: vertices within a SCC
'''
def second_pass_dfs(T_graph, start_vertex, seen):
    edges = T_graph.edges(start_vertex)
    seen[start_vertex] = True
    scc = [start_vertex]
    for v in edges:
        if not seen[v]:
            # TODO: fix the logic here
            scc.append(second_pass_dfs(T_graph, v, seen))
    return scc


def sccs(g):
    # YOUR SOLUTION HERE
    '''
    Obtain the finish order of the og graph
    NOTE: index in results = vertex id
    '''
    og_ordering = g.dfs()

    # Reverse the edges to obtain the transposed (T_graph)
    T_graph = transpose_graph(g)
    reset_color(og_ordering) # might not be needed

    # Run DFS again in reverse finished order
    reverse_order = extract_reverse_order(og_ordering, g) 
    seen = [False] * g.size()
    sccs = []
    for v in reverse_order:
        if not seen[v]:
            sccs.append(second_pass_dfs(T_graph, v, seen))
    return sccs
