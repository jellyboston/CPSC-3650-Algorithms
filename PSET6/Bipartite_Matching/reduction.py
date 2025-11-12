import graph
from flow_graph import FlowGraph

def bipartite_to_flow(g, n, m):
    """ Creates a flow graph such that the maximum flow in the flow
        graph corresponds to a maximum atching in the given bipartite
        graph.  Returns a triple containing the flow graph and
        the indices of the source and sink vertices in it.

        g -- a bipartite graph with vertices 0,...,n-1 on the left
             and n, ..., n+m on the right
        n -- a positive integer for the number of vertices on the left
        m -- a positive integer for the number of vertices on the right
    """
    # YOUR SOLUTION HERE
    flow_G = FlowGraph(n+m+2) # src and sink (+2)

    # add a source node s
    S = n + m # assigned after original indices to avoid collisions
    for v in range(0, n):
        flow_G.add_edge(S, v, 1) # assign capacity = 1 simultaneously
    
    # add sink node t (assigned after S)
    T = S + 1
    for v in range(n, n + m):
        flow_G.add_edge(v, T, 1)

    # add connections from the original bp graph
    for u in range(0, n):
        for v in g.edges(u):
            # enforce: v is in right only (l->v)
            if v >= n and v < n + m:
                flow_G.add_edge(u, v, 1)
    
    return flow_G, S, T


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
    # loop over vertices in left
    S, T = source, sink
    matching = []
    for u in range (0, n):
        for e in g.edges(u): # e becomes HalfEdge type
            # pick out neighbors on the right
            v = e.destination()
            if v >= n and v < n + m:
                # if cap is 1, then we know not a backward edge
                if e.capacity() == 1 and e.flow() == 1:
                    matching.append((u,v))
    return matching
