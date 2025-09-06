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

def extract_reverse_finished(og_ordering):
    assert g.size == len(og_ordering), "use interchangeably"
    reverse = [[] for i in range(g.size)]
    for i in range(g.size):
        reverse[i] = og_ordering[i].f
    reverse.sort(reverse=True)


def sccs(g):
    # YOUR SOLUTION HERE
    # Obtain the finish order of the og graph
    og_ordering = g.dfs()

    # Reverse the edges to obtain the transposed (T_graph)
    T_graph = transpose_graph(g)
    reset_color(og_ordering) # might not be needed

    # Run DFS again in reverse finished order
    reverse = extract_reverse_finished(og_ordering) # FIX
    '''
    TODO: fix this reverse! (see cg)
    '''





    return []
