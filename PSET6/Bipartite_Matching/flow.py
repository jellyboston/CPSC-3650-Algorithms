from collections import deque

from flow_graph import FlowGraph
import update

def find_augmenting_path(g, s, t, cond):
    """ Finds an augmenting path from s to t in the given flow graph.
        Returns the path as a list of edges, or None if there is no
        augmenting path.

        g -- a flow graph
        s -- the index of the source vertex in g
        t -- the index of the sink vertex in g
        cond -- a function that takes an edge and returns true or false
                used to determine which edges to allow in augmenting paths
    """
    n = g.size()

    # initialize status of vertices; 0=unseen, 1=in queue, 2=finished
    status = [0] * n

    # initialize pred (the *edge* used to get to each vertex)
    pred = [None] * n

    # add source vertex to queue
    q = deque()
    q.append(s)
    status[s] = 1

    while len(q) > 0 and status[t] == 0:
        u = q.popleft()
        for e in g.edges(u):
            if cond(e) and status[e.destination()] == 0:
                v = e.destination()
                status[v] = 1
                pred[v] = e
                q.append(v)
    if status[t] != 0:
        # found a path to sink; follow pred links to recreate it
        path = []
        curr = t
        while curr != s:
            path.append(pred[curr])
            curr = pred[curr].source()
        path.reverse()
        return path
    else:
        # no path from source to sink
        return None

    
def ford_fulkerson(g, s, t, cond=lambda e: e.residual() > 0):
    """ Augments the flow in the gven graph to be a maximum
        flow.

        g -- a flow graph
        s -- the index of the source vertex in g
        t -- the index of the sink vertex in g
        cond -- a function that takes an edge and returns true or false
                used to determine which edges to allow in augmenting paths;
                defaults to allowing any edge with positive residual
                capacity
    """
    p = find_augmenting_path(g, s, t, cond)
    while p is not None:
        # find residual capacity of bottleneck
        b = min(e.residual() for e in p)

        # update flow and residuals
        for e in p:
            update.update(e, e.opposite(), b)

        p = find_augmenting_path(g, s, t, cond)
