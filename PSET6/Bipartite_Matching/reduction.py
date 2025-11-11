import graph
from flow_graph import FlowGraph

def bipartite_to_flow(g, n, m):
    """ Creates a flow graph such that the maximum flow in the flow
        graph corresponds to a maximum atching in the given bipartite
        graph.  Returns a triple containing the flow graph and
        the indices of the source and sink vertices in it.

        g -- a bipartite graph with vertices 0,...,n-1 on the right
             and n, ..., n+m on the left
        n -- a positive integer for the number of vertices on the left
        m -- a positive integer for the number of vertices on the right
    """
    # YOUR SOLUTION HERE
    '''
    1. make into DAG
    2. add src (S) and dst (t) --> directed edges from each to every node
    3. add weights of 1 to every link 

    Ford-Fulkerson Algorithm
    - Set reverse edges to weight 0 (make bi-directional)
    - Find augmenting path (simple path from source to the sink; can use DFS/BFS)
    - 
    '''

    return FlowGraph(n+m), n + m, n + m + 1


def flow_to_matching(g, source, sink, n, m):
    """ Returns a list of (u, v) pairs giving the matching corresponding to the flow
        in g.

        g -- a graph returned from bipartite_to_flow with n vertices on the left
             and m on the right
        source -- the index of the source vertex in g
        sink -- the index of the sink vertex in g
        n -- a positive integer for the number of vertices on the left
        m -- a positive integer for the number of vertices on the right
    """
    # YOUR SOLUTION HERE
    return []
